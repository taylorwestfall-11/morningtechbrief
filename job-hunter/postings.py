#!/usr/bin/env python3
"""Cache the raw text of each live posting to job-hunter/postings/<id>.txt.

Run:  python job-hunter/postings.py

Why: the dashboard's "Copy posting" button feeds a job description into another
AI to tailor a resume. A static page cannot fetch a posting itself (CORS), and
the text is far too big to inline into the page -- 31 live roles would add ~150KB
to something already loaded on a phone. So the text is cached here, one file per
role, and the button fetches it same-origin on demand.

Only fetches roles it doesn't already have, so the daily cost is new roles only.

Text quality, best source first:
  1. ATS JSON APIs (Greenhouse/Lever) -- the real description, cleanly delimited,
     and they never bot-block. This is why an employer ATS link beats an
     aggregator link twice over.
  2. schema.org JobPosting `description` -- present on roughly 1 in 3 postings.
  3. A readability-ish pass over the HTML -- last resort, noisy.
Roles whose site blocks us (403, ~45% from a CI runner) simply get no file, and
the button falls back to a summary plus the URL.
"""
import html as html_mod
import json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
JOBS = os.path.join(HERE, "jobs.json")
OUT = os.path.join(HERE, "postings")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/122 Safari/537.36")

MIN_CHARS = 400      # below this it's a nav bar or an error page, not a posting
MAX_CHARS = 24000    # generous for a real posting; keeps a runaway page bounded

ATS = [
    (re.compile(r"(?:job-)?boards\.greenhouse\.io/(?:embed/job_app\?for=)?([\w.-]+)/jobs/(\d+)"),
     lambda m: ("gh", "https://boards-api.greenhouse.io/v1/boards/%s/jobs/%s"
                % (m.group(1), m.group(2)))),
    (re.compile(r"jobs\.lever\.co/([\w.-]+)/([0-9a-fA-F-]{36})"),
     lambda m: ("lever", "https://api.lever.co/v0/postings/%s/%s?mode=json"
                % (m.group(1), m.group(2)))),
]


def curl(url):
    try:
        p = subprocess.run(["curl", "-sL", "--compressed", "--max-time", "20", "-A", UA, url],
                           capture_output=True, timeout=30)
        return p.stdout.decode("utf-8", "replace")
    except Exception:
        return ""


# Aggregators prepend their own furniture to a description. It isn't the job.
BOILERPLATE = re.compile(
    r"(?im)^\s*(this job might no longer be available\.?"
    r"|apply now\.?|share this job\.?|back to (jobs|search)\.?)\s*$")


def detag(s):
    """HTML fragment -> readable plain text, keeping list and paragraph breaks.

    Unescape BEFORE stripping tags. Greenhouse's `content` is HTML-*escaped* HTML
    (&lt;p&gt;...), so stripping first matches nothing and the later unescape then
    *creates* the tags -- 187 of them leaked into one cached posting that way.
    Unescape again at the end for entities that live inside the text (&amp;nbsp;).
    """
    s = html_mod.unescape(s)
    s = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", s)
    s = re.sub(r"(?i)<li[^>]*>", "\n• ", s)
    s = re.sub(r"(?i)<(br|/p|/div|/h[1-6]|/li|/tr)[^>]*>", "\n", s)
    s = re.sub(r"(?s)<[^>]+>", " ", s)
    s = html_mod.unescape(s)
    s = BOILERPLATE.sub("", s)
    s = re.sub(r"[ \t\xa0]+", " ", s)
    s = re.sub(r"\n\s*\n\s*\n+", "\n\n", s)
    return "\n".join(line.strip() for line in s.split("\n")).strip()


def from_ats(url):
    for pat, build in ATS:
        m = pat.search(url)
        if not m:
            continue
        kind, api = build(m)
        raw = curl(api)
        if not raw:
            return ""
        try:
            d = json.loads(raw)
        except Exception:
            return ""
        if kind == "gh":
            return detag(d.get("content") or "")
        parts = []
        if d.get("descriptionPlain"):
            parts.append(d["descriptionPlain"])
        elif d.get("description"):
            parts.append(detag(d["description"]))
        for L in d.get("lists") or []:
            parts.append("\n" + (L.get("text") or "") + "\n" + detag(L.get("content") or ""))
        if d.get("additionalPlain"):
            parts.append(d["additionalPlain"])
        return "\n".join(parts).strip()
    return ""


def from_jsonld(page):
    for m in re.finditer(r'(?is)<script[^>]+application/ld\+json[^>]*>(.*?)</script>', page):
        try:
            blob = json.loads(m.group(1).strip())
        except Exception:
            continue
        stack = blob if isinstance(blob, list) else [blob]
        while stack:
            node = stack.pop(0)
            if isinstance(node, list):
                stack = list(node) + stack
                continue
            if not isinstance(node, dict):
                continue
            if isinstance(node.get("@graph"), list):
                stack = list(node["@graph"]) + stack
                continue
            if node.get("@type") == "JobPosting" and node.get("description"):
                return detag(node["description"])
    return ""


def from_html(page):
    """Last resort: the densest <main>/<article>/role=main block, else the body."""
    for pat in (r"(?is)<main[^>]*>(.*?)</main>",
                r"(?is)<article[^>]*>(.*?)</article>",
                r'(?is)<div[^>]+role="main"[^>]*>(.*?)</div>'):
        m = re.search(pat, page)
        if m:
            t = detag(m.group(1))
            if len(t) >= MIN_CHARS:
                return t
    m = re.search(r"(?is)<body[^>]*>(.*?)</body>", page)
    return detag(m.group(1)) if m else ""


# Scraping a JS-rendered posting with curl silently returns the careers INDEX --
# nav, filters, every open role -- and it's several KB, so length alone reads as
# success. Three Riot roles each cached 18,481 chars of "Open Positions: 156 |
# Select a Craft | Accounting Admin Art...". Junk text is worse than none here:
# the whole point is pasting a description into another AI to tailor a resume,
# and a careers index would poison that silently. So anything scraped has to
# prove it's actually a job description.
INDEX_MARKERS = ["open positions", "select a craft", "filter by", "sort by",
                 "jobs found", "search jobs", "all departments", "browse careers",
                 "no results", "refine your search", "job alerts"]
POSTING_MARKERS = ["responsibilit", "qualification", "requirement", "you'll", "you will",
                   "we're looking", "about the role", "what you", "experience in",
                   "benefits", "compensation", "your impact", "who you are",
                   "minimum", "preferred", "day-to-day"]
GENERIC_TITLE_WORDS = {"senior", "manager", "director", "quality", "assurance", "lead",
                       "head", "staff", "principal", "engineering", "development",
                       "associate", "studio", "global", "operations", "technical"}


def looks_like_posting(text, job):
    """-> (ok, reason). Applied to scraped text; ATS APIs are keyed by job id and
    can't return the wrong role, so they skip this."""
    low = text.lower()
    if sum(1 for m in INDEX_MARKERS if m in low) >= 2:
        return False, "reads like a careers index"
    if sum(1 for m in POSTING_MARKERS if m in low) < 2:
        return False, "no job-description language"
    distinctive = [w for w in re.findall(r"[A-Za-z]{4,}", job.get("title", ""))
                   if w.lower() not in GENERIC_TITLE_WORDS]
    if distinctive and not any(w.lower() in low for w in distinctive):
        return False, "doesn't mention %s" % "/".join(distinctive[:2])
    return True, ""


def text_for(job):
    url = job.get("url", "")
    if not url:
        return "", "no-url"

    # ATS APIs are addressed by job id -- they cannot hand back a different role.
    t = from_ats(url)
    if len(t) >= MIN_CHARS:
        return t, "ats-api"

    page = curl(url)
    if not page:
        return "", "unreachable"

    for extract, label in ((from_jsonld, "json-ld"), (from_html, "html")):
        t = extract(page)
        if len(t) < MIN_CHARS:
            continue
        ok, why = looks_like_posting(t, job)
        if ok:
            return t, label
        print("      rejected %s text: %s" % (label, why))
    return "", "no usable text"


def main():
    os.makedirs(OUT, exist_ok=True)
    with open(JOBS, encoding="utf-8") as f:
        data = json.load(f)

    live = [j for j in data["jobs"] if not j.get("closed")]
    live_ids = {j["id"] for j in live}
    got = skipped = failed = 0

    for job in live:
        path = os.path.join(OUT, job["id"] + ".txt")
        if os.path.exists(path):
            skipped += 1
            continue
        text, how = text_for(job)
        if not text:
            print("  no text [%s] %s" % (how, job["id"]))
            failed += 1
            continue
        header = "\n".join(x for x in [
            job.get("title", ""),
            job.get("company", ""),
            job.get("location", ""),
            ("Compensation: " + job["salary"]) if job.get("salary") else "",
            ("Posted: " + job["date_posted"]) if job.get("date_posted") else "",
            job.get("url", ""),
        ] if x)
        body = text[:MAX_CHARS]
        # newline="\n": Python's text mode writes CRLF on Windows, which broke the
        # page's separator match (it looks for \n------\n) and duplicated the
        # header into every copied posting. Also keeps the repo LF-only.
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(header + "\n\n" + ("-" * 60) + "\n\n" + body + "\n")
        print("  cached [%s] %s (%d chars)" % (how, job["id"], len(body)))
        got += 1

    # Drop text for roles that are closed or gone -- no point serving a dead
    # posting, and it keeps the repo from growing forever.
    removed = 0
    for fn in os.listdir(OUT):
        if fn.endswith(".txt") and fn[:-4] not in live_ids:
            os.remove(os.path.join(OUT, fn))
            removed += 1

    print("\ncached %d new | %d already had text | %d unavailable | %d pruned"
          % (got, skipped, failed, removed))


if __name__ == "__main__":
    main()

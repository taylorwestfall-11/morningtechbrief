#!/usr/bin/env python3
"""Turn URLs pasted from the phone into real job entries. No LLM -- curl + stdlib.

Run:  python job-hunter/enrich.py

Why this exists on the server side: the dashboard is a static page, and a browser
cannot fetch an arbitrary job posting from it -- CORS forbids it. So "add by URL"
writes the link to job-hunter/inbox.json, and this fills in the rest here.

Fit score is deliberately left null: scoring needs judgment, so the daily AI scan
fills it in. The card is useful before then.

Consumed items are removed from the inbox. Anything that fails to fetch is KEPT,
so a flaky network retries tomorrow rather than silently losing the link.
"""
import json, os, re, subprocess, urllib.parse
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
JOBS = os.path.join(HERE, "jobs.json")
INBOX = os.path.join(HERE, "inbox.json")
TODAY = datetime.now(timezone.utc).strftime("%Y-%m-%d")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/122 Safari/537.36")

MAX_TRIES = 5   # give up on a URL that has failed this many days running


def fetch(url):
    try:
        p = subprocess.run(["curl", "-sL", "--compressed", "--max-time", "15",
                            "-A", UA, url], capture_output=True, timeout=25)
        return p.stdout.decode("utf-8", "replace")
    except Exception:
        return ""


def slug(*parts):
    s = "-".join(p for p in parts if p).lower()
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", s)).strip("-")[:80]


def first_str(v):
    if isinstance(v, str):
        return v
    if isinstance(v, dict):
        return v.get("name") or ""
    if isinstance(v, list) and v:
        return first_str(v[0])
    return ""


def from_jsonld(html):
    """Most real postings embed a schema.org JobPosting. Use it where present."""
    for m in re.finditer(r'(?is)<script[^>]+application/ld\+json[^>]*>(.*?)</script>', html):
        try:
            blob = json.loads(m.group(1).strip())
        except Exception:
            continue
        stack = blob if isinstance(blob, list) else [blob]
        for node in stack:
            if not isinstance(node, dict):
                continue
            if "@graph" in node and isinstance(node["@graph"], list):
                stack = stack + node["@graph"]
                continue
            if node.get("@type") != "JobPosting":
                continue
            loc = node.get("jobLocation")
            if isinstance(loc, list):
                loc = loc[0] if loc else {}
            addr = (loc or {}).get("address") if isinstance(loc, dict) else {}
            addr = addr if isinstance(addr, dict) else {}
            val = ((node.get("baseSalary") or {}).get("value")
                   if isinstance(node.get("baseSalary"), dict) else {}) or {}
            lo, hi = val.get("minValue"), val.get("maxValue")
            remote = "remote" if node.get("jobLocationType") == "TELECOMMUTE" else ""
            return {
                "title": (node.get("title") or "").strip(),
                "company": first_str(node.get("hiringOrganization")).strip(),
                "location": ", ".join(x for x in [addr.get("addressLocality"),
                                                  addr.get("addressRegion")] if x),
                "date_posted": (node.get("datePosted") or "")[:10],
                "salary": ("%s-%s" % (lo, hi)) if lo and hi else "",
                "remote": remote,
            }
    return {}


# Only ~1 in 3 real postings ships JSON-LD, so <title> is the usual fallback --
# but on a bot-blocked or interstitial page the title is junk, and junk becomes a
# job title. Measured on real postings: "Just a moment...", "Security Check -
# Indeed.com", "wellfound.com". Better a placeholder the AI scan fixes tomorrow
# than a board full of roles called "Just a moment...".
JUNK_TITLE = re.compile(
    r"(?i)^\s*(just a moment|security check|attention required|access denied|"
    r"are you a robot|please wait|checking your browser|robot check|"
    r"403|404|forbidden|not found|error|sign in|log ?in|loading)\b"
    r"|cloudflare|captcha"
    r"|^\s*(www\.)?[\w.-]+\.(com|io|co|net|org)\s*$")   # a bare domain isn't a title


def title_tag(html):
    m = re.search(r"(?is)<title[^>]*>(.*?)</title>", html)
    if not m:
        return ""
    t = re.sub(r"\s+", " ", re.sub(r"(?s)<[^>]+>", "", m.group(1))).strip()
    return "" if JUNK_TITLE.search(t) else t


def main():
    if not os.path.exists(INBOX):
        print("no inbox.json — nothing to do")
        return
    with open(INBOX, encoding="utf-8") as f:
        inbox = json.load(f)
    with open(JOBS, encoding="utf-8") as f:
        data = json.load(f)

    items = inbox.get("items") or []
    if not items:
        print("inbox empty")
        return

    have_urls = {j.get("url") for j in data["jobs"]}
    have_ids = {j["id"] for j in data["jobs"]}
    keep, added = [], 0

    for item in items:
        url = (item.get("url") or "").strip()
        if not url:
            continue
        if url in have_urls:
            print("SKIP already tracked: %s" % url[:70])
            continue

        html = fetch(url)
        if not html:
            item["tries"] = item.get("tries", 0) + 1
            if item["tries"] >= MAX_TRIES:
                print("DROP unreachable after %d tries: %s" % (item["tries"], url[:60]))
            else:
                print("RETRY later (%dx): %s" % (item["tries"], url[:60]))
                keep.append(item)
            continue

        meta = from_jsonld(html)
        # What the user typed always wins -- they looked at the page, we didn't.
        title = item.get("title") or meta.get("title") or title_tag(html)[:90]
        company = item.get("company") or meta.get("company")
        # No usable name? Still add it -- they asked for it -- but label it from the
        # URL and let the daily AI scan fill in the real title and fit score.
        named = bool(title and company)
        if not title:
            title = "Untitled role (from link)"
        if not company:
            company = urllib.parse.urlparse(url).netloc.replace("www.", "") or "Unknown"
        jid = slug(company, title) if named else slug(company, os.path.basename(
            urllib.parse.urlparse(url).path.rstrip("/")) or "posting")
        if jid in have_ids:
            print("SKIP duplicate id: %s" % jid)
            continue

        data["jobs"].append({
            "id": jid,
            "title": title,
            "company": company,
            "category": item.get("category") or "",
            "location": meta.get("location", ""),
            "remote": item.get("remote") or meta.get("remote", ""),
            "salary": meta.get("salary", ""),
            "source": "added by hand",
            "url": url,
            "date_found": item.get("added") or TODAY,
            "date_posted": meta.get("date_posted", ""),
            "notes": "",
            "closed": False,
            "fit": None,
        })
        have_ids.add(jid)
        have_urls.add(url)
        added += 1
        print("ADDED %s" % jid)

    inbox["items"] = keep
    with open(INBOX, "w", encoding="utf-8") as f:
        json.dump(inbox, f, ensure_ascii=False, indent=2)
    with open(JOBS, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("enriched %d | %d left in the inbox" % (added, len(keep)))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Deterministic dead-link sweep for the job tracker. No LLM -- curl + stdlib only.

Run:  python job-hunter/deadlink_check.py

Rules validated 2026-07-15 against 46 real postings (13/13 dead caught, 0/46 live
touched). Several are counter-intuitive. Before "cleaning this up", read these:

  * curl, NOT urllib. urllib fails TLS/redirect handshakes that curl and browsers
    pass, on real job sites (netflix/remotegamejobs among them). Tested.
  * READ THE BODY. Aggregators (Built In, GamesJobsDirect) serve HTTP 200, at the
    original URL, with the original <title>, and a body saying "Sorry, this job was
    removed at 10:20 a.m.". Status-code-only checking misses ~85% of real deaths --
    that is why dead roles kept reaching the board.
  * Do NOT add an "only dead if the page lacks an Apply button" guard. It was tested
    and it FAILS: Built In's removed-job pages still say "Apply Now" in the nav and
    in adjacent listings, so the guard spares 9 of 11 real deaths. The phrase list
    below needs no guard -- it fired on 0 of 46 live postings.
  * 403/429 are bot-blocks, never deaths. Closing them loses real jobs.
  * Only ever ADD a closed flag. Never un-close, never delete, never renumber an id
    -- ids are the keys the dashboard stores "I applied to this" under.
  * Applied/tracked roles stay visible in the UI even when closed, so closing is safe.
"""
import json, os, re, subprocess, urllib.parse
from datetime import datetime, timedelta, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
JOBS = os.path.join(HERE, "jobs.json")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/122 Safari/537.36")
NOW = datetime.now(timezone.utc)
TODAY = NOW.strftime("%Y-%m-%d")

# Close on sight. Specific enough to be safe; 0 false positives across 46 postings.
DECISIVE = [
    "sorry, this job was removed", "this job was removed",
    "this job has expired", "job has expired", "vacancy has expired",
    "no longer accepting application", "applications are closed",
    "position has been filled", "role has been filled",
    "this job is closed", "posting is closed", "job posting is no longer",
]
# Real signals, but likelier to appear innocently. Need a second signal (thin page).
GENERIC = ["no longer available", "job not found", "position is no longer available"]

DEAD_URL_MARKERS = ["error=true", "not_found=true", "not-found", "notfound",
                    "/oops", "job-not-found", "no-longer-available", "jobnotfound"]

# A redirect landing on one of these = the specific posting is gone.
ROOT_PATHS = {"", "/careers", "/jobs", "/job", "/positions", "/openings", "/search",
              "/en", "/us/en", "/global/en", "/en-us", "/careers/search",
              "/en/careers", "/company/careers", "/careers/jobs", "/join-us"}

# ATS JSON APIs = GROUND TRUTH: they answer honestly, don't bot-block, and 404 the
# moment a posting is pulled. Verified: greenhouse live->200 / pulled->404, lever->404.
# Always prefer an API over guessing at HTML. Add more as you meet them.
ATS_API = [
    (re.compile(r"(?:job-)?boards\.greenhouse\.io/(?:embed/job_app\?for=)?([\w.-]+)/jobs/(\d+)"),
     lambda m: "https://boards-api.greenhouse.io/v1/boards/%s/jobs/%s" % (m.group(1), m.group(2))),
    (re.compile(r"jobs\.lever\.co/([\w.-]+)/([0-9a-fA-F-]{36})"),
     lambda m: "https://api.lever.co/v0/postings/%s/%s?mode=json" % (m.group(1), m.group(2))),
]

# A bot-block is NOT evidence of death, and repeated bot-blocks are not evidence
# either -- they just mean the host always blocks this IP. Measured 2026-07-15:
# the same sweep saw 4 x 403 from a home IP and 14 x 403 from a GitHub runner,
# including live Riot/Epic/Ubisoft postings. An "auto-close after N failures"
# rule would therefore have deleted live roles off the board within a week.
#
# So: unverifiable NEVER auto-closes. We only ever close on positive evidence
# (404/410, a soft-404 phrase, or a redirect to a careers root). Unverified roles
# get a badge and a "how long since we could check" counter, and the human is the
# final oracle via the report-dead button. Rotting-but-labelled beats silently
# deleting a real job.


def curl(url):
    """-> (http_code|None, final_url, body). None means the request itself failed."""
    try:
        p = subprocess.run(
            ["curl", "-sL", "--compressed", "--max-time", "15", "-A", UA,
             "-H", "Accept-Language: en-US,en;q=0.9",
             "-w", "\n__M__%{http_code} %{url_effective}", url],
            capture_output=True, timeout=25)
        out = p.stdout.decode("utf-8", "replace")
    except Exception:
        return None, url, ""
    body, _, meta = out.rpartition("\n__M__")
    code, _, final = meta.partition(" ")
    try:
        code = int(code)
    except ValueError:
        code = None
    return code, final.strip() or url, body


def text_of(html):
    html = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", html)
    return re.sub(r"\s+", " ", re.sub(r"(?s)<[^>]+>", " ", html)).lower()


def ats_url(url):
    for pat, build in ATS_API:
        m = pat.search(url)
        if m:
            return build(m)
    return None


# ── posting age ──────────────────────────────────────────────────────────────
# The other half of "is this worth showing": a live link to a role posted two
# years ago is still junk. date_posted arrives from the LLM scan and is filled
# only ~1 in 4 times, sometimes with an aggregator's stale original date. This
# sweep already fetches every posting and every ATS API, so it is the one place
# that can read the real date off the live page. It writes date_posted only when
# it finds something it trusts MORE than what's there -- never blanks a value.
#
# Trust order (higher wins): an ATS API's own timestamp > a JobPosting JSON-LD
# datePosted embedded in the page > a "posted N days ago" phrase in the body >
# whatever the scan guessed. The dashboard turns the date into an age and hides
# roles past the cutoff; our job is just to make the date as true as we can.
TRUST = {"": 0, "scan": 0, "relative": 1, "jsonld": 2, "greenhouse": 3, "lever": 3}


def _iso(s):
    """Pull a clean YYYY-MM-DD out of an ISO-ish string; '' if it isn't one."""
    m = re.match(r"\s*(\d{4}-\d{2}-\d{2})", str(s or ""))
    return m.group(1) if m else ""


def date_from_ats(api, body):
    """(date, source) from a Greenhouse/Lever API body we already fetched."""
    try:
        obj = json.loads(body)
    except Exception:
        return "", ""
    if "greenhouse" in api:
        d = _iso(obj.get("first_published") or obj.get("updated_at"))
        return (d, "greenhouse") if d else ("", "")
    if "lever" in api:
        ms = obj.get("createdAt")
        if isinstance(ms, (int, float)):
            return (datetime.fromtimestamp(ms / 1000, timezone.utc)
                    .strftime("%Y-%m-%d"), "lever")
    return "", ""


def date_from_jsonld(html):
    """datePosted from a schema.org JobPosting embedded in the page."""
    for m in re.finditer(r'(?is)<script[^>]+application/ld\+json[^>]*>(.*?)</script>', html):
        try:
            blob = json.loads(m.group(1).strip())
        except Exception:
            continue
        stack = blob if isinstance(blob, list) else [blob]
        while stack:
            node = stack.pop()
            if not isinstance(node, dict):
                continue
            if isinstance(node.get("@graph"), list):
                stack.extend(node["@graph"])
            if node.get("@type") == "JobPosting":
                d = _iso(node.get("datePosted"))
                if d:
                    return d, "jsonld"
    return "", ""


# "Posted 3 days ago", "Posted 30+ days ago", "2 weeks ago", "posted yesterday".
# Aggregators (gamejobs.co, remotegamejobs, hitmarker) lean on these instead of
# JSON-LD. We resolve them against today's date into a concrete YYYY-MM-DD.
_REL = re.compile(r"(?i)(?:posted\s+)?(\d+)\+?\s*(day|week|month|hour|minute)s?\s+ago")
_ABS = re.compile(r"(?i)posted(?:\s+on)?[:\s]+"
                  r"(\d{4}-\d{2}-\d{2}|[A-Z][a-z]{2,8}\.?\s+\d{1,2},?\s+\d{4})")
_MONTHS = {m: i for i, m in enumerate(
    ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], 1)}


def date_from_text(text):
    """(date, 'relative') from a posted-N-ago / posted-on-DATE phrase, else ''."""
    if "posted yesterday" in text:
        return (NOW - timedelta(days=1)).strftime("%Y-%m-%d"), "relative"
    if re.search(r"(?i)posted\s+today|just posted", text):
        return TODAY, "relative"
    m = _ABS.search(text)
    if m:
        raw = m.group(1)
        if _iso(raw):
            return _iso(raw), "relative"
        mm = re.match(r"([A-Za-z]+)\.?\s+(\d{1,2}),?\s+(\d{4})", raw)
        if mm and mm.group(1)[:3].lower() in _MONTHS:
            try:
                return (datetime(int(mm.group(3)), _MONTHS[mm.group(1)[:3].lower()],
                                 int(mm.group(2))).strftime("%Y-%m-%d"), "relative")
            except ValueError:
                pass
    m = _REL.search(text)
    if m:
        n, unit = int(m.group(1)), m.group(2).lower()
        days = {"minute": 0, "hour": 0, "day": 1, "week": 7, "month": 30}[unit] * n
        return (NOW - timedelta(days=days)).strftime("%Y-%m-%d"), "relative"
    return "", ""


def classify(url):
    """-> (verdict, reason, date, date_src). date_src is '' when we found none.
    date/date_src carry the most-trusted posting date this run could establish,
    from the same fetches the liveness check already makes."""
    if not url:
        return "dead", "no-url", "", ""

    posted, psrc = "", ""
    api = ats_url(url)
    if api:
        code, _, abody = curl(api)
        if code == 200:
            posted, psrc = date_from_ats(api, abody)
            reason = "ats-api"
            # An ATS 200 is authoritative liveness AND date; still read the HTML
            # below only to keep behaviour identical when the API is ambiguous.
            return "live", reason, posted, psrc
        if code in (404, 410):
            return "dead", "ats-api-%s" % code, "", ""
        # anything else: fall through and judge the HTML

    code, final, body = curl(url)
    if code is None:
        return "unverified", "request-failed", "", ""
    if code in (404, 410):
        return "dead", str(code), "", ""
    if code in (403, 429) or code >= 500:
        return "unverified", str(code), "", ""

    if any(m in final.lower() for m in DEAD_URL_MARKERS):
        return "dead", "error-url", "", ""

    path = urllib.parse.urlparse(final).path.rstrip("/").lower()
    if path in {p.rstrip("/") for p in ROOT_PATHS}:
        return "dead", "redirect-to-root", "", ""

    text = text_of(body)
    hit = next((p for p in DECISIVE if p in text), None)
    if hit:
        return "dead", "soft-404: %s" % hit, "", ""

    hit = next((p for p in GENERIC if p in text), None)
    if hit and len(text) < 2500:          # a generic phrase on a near-empty page
        return "dead", "soft-404(thin): %s" % hit, "", ""

    # Live. Best date we can read off the page: JSON-LD beats a relative phrase.
    posted, psrc = date_from_jsonld(body)
    if not posted:
        posted, psrc = date_from_text(text)
    return "live", str(code), posted, psrc


def main():
    with open(JOBS, encoding="utf-8") as f:
        data = json.load(f)

    checked = closed = dated = 0
    for job in data["jobs"]:
        if job.get("closed"):
            continue
        checked += 1
        verdict, reason, posted, psrc = classify(job.get("url", ""))
        job["last_checked"] = TODAY

        # Record the date whenever this run trusts its source at least as much as
        # whatever filled date_posted before. First real date on an undated role
        # counts too (old trust is "" -> 0). Never blanks an existing value.
        if posted and TRUST.get(psrc, 0) >= TRUST.get(job.get("date_src", ""), 0):
            if job.get("date_posted") != posted or job.get("date_src") != psrc:
                job["date_posted"], job["date_src"] = posted, psrc
                dated += 1
                print("  dated [%s] %s -> %s" % (psrc, job["id"], posted))

        if verdict == "live":
            job["check_fails"] = 0
            job.pop("unverified", None)
            job.pop("unverified_since", None)

        elif verdict == "unverified":
            # Never closes -- see the bot-block note above. This counter feeds the
            # UI badge only; it is never a liveness decision.
            job["check_fails"] = job.get("check_fails", 0) + 1
            job["unverified"] = reason
            job.setdefault("unverified_since", TODAY)
            print("  unverified [%s] %s (%dx since %s)"
                  % (reason, job["id"], job["check_fails"], job["unverified_since"]))

        else:  # dead
            job.update(closed=True, closed_on=TODAY,
                       closed_reason="Dead link: %s" % reason)
            closed += 1
            print("CLOSED [%s] %s" % (reason, job["id"]))

    total_closed = sum(1 for j in data["jobs"] if j.get("closed"))
    with open(JOBS, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("\nchecked %d | newly closed %d | dates updated %d | total closed %d | live %d"
          % (checked, closed, dated, total_closed, len(data["jobs"]) - total_closed))


if __name__ == "__main__":
    main()

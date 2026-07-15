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
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
JOBS = os.path.join(HERE, "jobs.json")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/122 Safari/537.36")
TODAY = datetime.now(timezone.utc).strftime("%Y-%m-%d")

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


def classify(url):
    """-> (verdict, reason) where verdict is live | dead | unverified."""
    if not url:
        return "dead", "no-url"

    api = ats_url(url)
    if api:
        code, _, _ = curl(api)
        if code == 200:
            return "live", "ats-api"
        if code in (404, 410):
            return "dead", "ats-api-%s" % code
        # anything else: fall through and judge the HTML

    code, final, body = curl(url)
    if code is None:
        return "unverified", "request-failed"
    if code in (404, 410):
        return "dead", str(code)
    if code in (403, 429) or code >= 500:
        return "unverified", str(code)

    if any(m in final.lower() for m in DEAD_URL_MARKERS):
        return "dead", "error-url"

    path = urllib.parse.urlparse(final).path.rstrip("/").lower()
    if path in {p.rstrip("/") for p in ROOT_PATHS}:
        return "dead", "redirect-to-root"

    text = text_of(body)
    hit = next((p for p in DECISIVE if p in text), None)
    if hit:
        return "dead", "soft-404: %s" % hit

    hit = next((p for p in GENERIC if p in text), None)
    if hit and len(text) < 2500:          # a generic phrase on a near-empty page
        return "dead", "soft-404(thin): %s" % hit

    return "live", str(code)


def main():
    with open(JOBS, encoding="utf-8") as f:
        data = json.load(f)

    checked = closed = 0
    for job in data["jobs"]:
        if job.get("closed"):
            continue
        checked += 1
        verdict, reason = classify(job.get("url", ""))
        job["last_checked"] = TODAY

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
    print("\nchecked %d | newly closed %d | total closed %d | live %d"
          % (checked, closed, total_closed, len(data["jobs"]) - total_closed))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Deterministic dead-link check for the QA job tracker.

Marks a job `"closed": true` when its apply URL no longer resolves to a live posting.
This is mechanical (curl + rules) rather than LLM judgment, because the model kept
adding dead links. Run from anywhere: `python job-hunter/deadlink_check.py`.

A posting is DEAD when, after following redirects:
  - HTTP status is 404 or 410; OR
  - the final URL contains an error marker (error=true, not_found=true, /oops, ...); OR
  - it redirected to a careers ROOT / listing page (path is empty or a known root).
HTTP 403/429 = bot-blocked = UNVERIFIABLE -> left as-is (never marked dead).
Never un-closes anything; only adds closed flags. Applied/tracked roles stay visible
in the UI even when closed (the dashboard keeps them), so closing here is safe.
"""
import json, subprocess, os, urllib.parse
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JP = os.path.join(ROOT, "job-hunter", "jobs.json")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120 Safari/537.36")
TODAY = datetime.now(timezone.utc).strftime("%Y-%m-%d")

DEAD_MARKERS = ["error=true", "not_found=true", "not-found", "notfound", "/oops",
                "no-longer-available", "job-not-found", "expired"]
# Final-path values that mean "bounced to the site root / generic listing" = posting gone.
ROOT_PATHS = {"", "/careers", "/careers/search", "/jobs", "/job", "/positions",
              "/openings", "/work-with-us/jobs", "/global/en", "/us/en", "/en",
              "/en/careers", "/en-us", "/company/careers", "/careers/jobs"}


def classify(url):
    if not url:
        return ("dead", "no-url")
    try:
        r = subprocess.run(
            ["curl", "-s", "-o", os.devnull, "-L", "--max-time", "12", "-A", UA,
             "-w", "%{http_code} %{url_effective}", url],
            capture_output=True, text=True, timeout=20).stdout.strip()
    except Exception:
        return ("unverified", "timeout")
    code, _, final = r.partition(" ")
    if code in ("404", "410"):
        return ("dead", code)
    if code in ("403", "429"):
        return ("unverified", code)          # bot-blocked; don't judge
    fl = final.lower()
    if any(m in fl for m in DEAD_MARKERS):
        return ("dead", "error-page")
    path = urllib.parse.urlparse(final).path.rstrip("/")
    if (path or "") in {p.rstrip("/") for p in ROOT_PATHS}:
        return ("dead", "redirect-to-root")
    return ("live", code)


def main():
    d = json.load(open(JP, encoding="utf-8"))
    checked = newly = 0
    for x in d["jobs"]:
        if x.get("closed"):
            continue
        checked += 1
        verdict, reason = classify(x.get("url", ""))
        if verdict == "dead":
            x["closed"] = True
            x["closed_on"] = TODAY
            x["closed_reason"] = f"Auto dead-link check: {reason}"
            newly += 1
            print(f"CLOSED [{reason}] {x['id']}")
    total_closed = sum(1 for x in d["jobs"] if x.get("closed"))
    json.dump(d, open(JP, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"checked {checked} live roles | newly closed {newly} | total closed {total_closed} "
          f"| live now {len(d['jobs']) - total_closed}")


if __name__ == "__main__":
    main()

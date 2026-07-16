#!/usr/bin/env python3
"""Render jobs-7m3k9q.html from the template + jobs.json + config.json. No LLM.

Run:  python job-hunter/build_page.py

This exists so nothing ever hand-edits the published page. The daily AI run used
to regenerate a 115KB file by rewriting the array between markers "while keeping
the localStorage status JavaScript byte-for-byte intact" -- a corruption waiting
to happen, and it silently reformatted the file at least once.

The AI's job is to append to jobs.json. Rendering is this script's job.

The template is the source of truth for markup; the output is disposable. If you
want to change the page, change job-hunter/template/dashboard.html.
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
TEMPLATE = os.path.join(HERE, "template", "dashboard.html")
JOBS = os.path.join(HERE, "jobs.json")
CONFIG = os.path.join(HERE, "config.json")
OUT = os.path.join(ROOT, "jobs-7m3k9q.html")

START, END = "/*__JOBS__*/", "/*__JOBS_END__*/"

# Fields the page never reads. Dropping them keeps the published file smaller and
# keeps internal bookkeeping out of a public repo.
STRIP = {"closed_on", "closed_reason", "check_fails", "last_checked", "unverified_since"}


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def main():
    for p in (TEMPLATE, JOBS, CONFIG):
        if not os.path.exists(p):
            sys.exit("FATAL: missing %s" % p)

    cfg = json.loads(read(CONFIG))
    data = json.loads(read(JOBS))
    html = read(TEMPLATE)

    if START not in html or END not in html:
        sys.exit("FATAL: jobs markers missing from the template -- refusing to write.")

    brand = cfg.get("branding", {})
    subs = {
        "{{TITLE}}": brand.get("title", "Job Tracker"),
        "{{EMOJI}}": brand.get("emoji", "\U0001F4BC"),
        "{{TAGLINE}}": cfg.get("candidate", {}).get("scope", ""),
        "{{LAST_SCAN}}": data.get("_meta", {}).get("last_scan", ""),
        "{{STATE_REPO}}": cfg.get("repos", {}).get("state", ""),
        "{{PUBLIC_REPO}}": cfg.get("repos", {}).get("public", ""),
    }
    for k, v in subs.items():
        html = html.replace(k, v)

    jobs = [{k: v for k, v in j.items() if k not in STRIP} for j in data["jobs"]]
    head, _, rest = html.partition(START)
    _, _, tail = rest.partition(END)
    html = head + START + json.dumps(jobs, ensure_ascii=False, indent=1) + END + tail

    leftover = [k for k in subs if k in html]
    if leftover:
        sys.exit("FATAL: unsubstituted placeholders %s -- refusing to write." % leftover)

    # The page is worthless if any of these silently vanish.
    for needle, what in [
        ('name="robots"', "noindex meta"),
        ('class="dailynav"', "phone nav bar"),
        ("jobhunter_state_v3", "status storage key"),
        ("function setStage", "stage handler"),
        ("function everEngaged", "the never-auto-hide invariant"),
        ("function mergeStates", "sync merge"),
        ('data-stage="', "per-card stage picker"),
    ]:
        if needle not in html:
            sys.exit("FATAL: %s is missing -- refusing to write." % what)

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(html)

    closed = sum(1 for j in data["jobs"] if j.get("closed"))
    print("built jobs-7m3k9q.html | %d jobs (%d live, %d closed) | last_scan %s | %d KB"
          % (len(data["jobs"]), len(data["jobs"]) - closed, closed,
             subs["{{LAST_SCAN}}"], os.path.getsize(OUT) // 1024))


if __name__ == "__main__":
    main()

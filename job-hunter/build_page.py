#!/usr/bin/env python3
"""Render jobs-7m3k9q.html from job-hunter/jobs.json. Deterministic; no LLM.

Run:  python job-hunter/build_page.py

This exists so nothing ever hand-edits the published page again. The daily AI run
used to regenerate a 115KB file by rewriting the array between markers "while
keeping the localStorage status JavaScript byte-for-byte intact" -- which is a
corruption waiting to happen, and which silently reformatted the file at least once.

The AI's job is to append to jobs.json. Rendering is this script's job.

Only two things are allowed to change: the JOBS array between the /*__JOBS__*/
markers, and the LAST_SCAN constant. Everything else -- the nav, the noindex meta,
the status/stage JavaScript -- is asserted unchanged before the file is written.
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
JOBS = os.path.join(HERE, "jobs.json")
PAGE = os.path.join(ROOT, "jobs-7m3k9q.html")

START, END = "/*__JOBS__*/", "/*__JOBS_END__*/"


def main():
    with open(JOBS, encoding="utf-8") as f:
        data = json.load(f)
    with open(PAGE, encoding="utf-8") as f:
        html = f.read()

    if START not in html or END not in html:
        sys.exit("FATAL: jobs array markers missing from the page -- refusing to write.")

    head, _, rest = html.partition(START)
    _, _, tail = rest.partition(END)

    last_scan = data.get("_meta", {}).get("last_scan", "")
    array = json.dumps(data["jobs"], ensure_ascii=False, indent=2)
    out = head + START + array + END + tail

    if last_scan:
        out, n = re.subn(r'const LAST_SCAN = "[^"]*";',
                         'const LAST_SCAN = "%s";' % last_scan, out, count=1)
        if n != 1:
            sys.exit("FATAL: could not set LAST_SCAN -- refusing to write.")

    # Guard rails: the parts that must survive verbatim.
    for needle, what in [
        ('name="robots"', "noindex meta"),
        ('class="dailynav"', "phone nav bar"),
        ('jobhunter_status_v2', "status storage key"),
        ('function setStage', "stage handler"),
        ('function render', "renderer"),
    ]:
        if needle not in out:
            sys.exit("FATAL: %s disappeared -- refusing to write." % what)

    # Nothing outside the array + LAST_SCAN may drift.
    def strip_dynamic(s):
        s = re.sub(re.escape(START) + r".*?" + re.escape(END), START + END, s, flags=re.S)
        return re.sub(r'const LAST_SCAN = "[^"]*";', "", s)

    if strip_dynamic(html) != strip_dynamic(out):
        sys.exit("FATAL: the page changed outside the jobs array -- refusing to write.")

    with open(PAGE, "w", encoding="utf-8") as f:
        f.write(out)

    closed = sum(1 for j in data["jobs"] if j.get("closed"))
    print("built jobs-7m3k9q.html | %d jobs (%d live, %d closed) | last_scan %s"
          % (len(data["jobs"]), len(data["jobs"]) - closed, closed, last_scan))


if __name__ == "__main__":
    main()

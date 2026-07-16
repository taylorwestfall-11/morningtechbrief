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
import json, os, re, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
TEMPLATE = os.path.join(HERE, "template", "dashboard.html")
JOBS = os.path.join(HERE, "jobs.json")
CONFIG = os.path.join(HERE, "config.json")
POSTINGS = os.path.join(HERE, "postings")
OUT = os.path.join(ROOT, "jobs-7m3k9q.html")

START, END = "/*__JOBS__*/", "/*__JOBS_END__*/"

# Fields the page never reads. Dropping them keeps the published file smaller and
# keeps internal bookkeeping out of a public repo.
STRIP = {"closed_on", "closed_reason", "check_fails", "last_checked", "unverified_since"}

# Closed roles are archive-only: you see them when hunting for something to
# re-mark, and that card shows a title, company, badges and the fit ring. It does
# NOT show the fit rationale or a cover-letter blurb for a job that no longer
# exists. Those two strings are 33 KB of the 106 KB array -- pure weight on every
# load, on a phone, for text nobody reads.
def slim(job):
    j = {k: v for k, v in job.items() if k not in STRIP}
    if isinstance(j.get("fit"), dict):
        # `blurb` backed the old cover-letter button, which is now "Copy job
        # posting". Nothing reads it, and it was ~20KB across the array.
        keep = ("score", "level") if j.get("closed") else ("score", "level", "why")
        j["fit"] = {k: v for k, v in j["fit"].items() if k in keep}
    if j.get("closed"):
        j.pop("notes", None)
    # Flag whether postings.py managed to cache this description, so the button
    # knows to fetch it rather than promising text that doesn't exist.
    if not j.get("closed") and os.path.exists(os.path.join(POSTINGS, j["id"] + ".txt")):
        j["txt"] = 1
    return j


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def check_js(html):
    """Refuse to publish a page whose JavaScript doesn't parse.

    The string assertions below only prove a name is PRESENT. They happily passed
    a build where one duplicated `let` killed the entire script: the page rendered
    its markup, showed zero jobs, and reported no error -- the failure looked like
    empty data. A parse check is the only thing that catches that class of bug.

    node isn't required to run this script (CI has it; a laptop may not), so this
    warns rather than blocks when node is missing.
    """
    m = re.search(r"<script>(.*)</script>", html, re.S)
    if not m:
        sys.exit("FATAL: no <script> block in the template -- refusing to write.")
    node = shutil.which("node")
    if not node:
        print("  note: node not found, skipping the JS syntax check")
        return
    tmp = None
    try:
        with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False,
                                         encoding="utf-8") as f:
            f.write(m.group(1))
            tmp = f.name
        r = subprocess.run([node, "--check", tmp], capture_output=True, text=True)
        if r.returncode != 0:
            err = (r.stderr or "").strip().splitlines()
            detail = "\n".join("    " + l for l in err[:6])
            sys.exit("FATAL: the page's JavaScript does not parse -- refusing to "
                     "write.\n%s" % detail)
    finally:
        if tmp and os.path.exists(tmp):
            os.unlink(tmp)


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

    jobs = [slim(j) for j in data["jobs"]]
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

    check_js(html)

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(html)

    closed = sum(1 for j in data["jobs"] if j.get("closed"))
    print("built jobs-7m3k9q.html | %d jobs (%d live, %d closed) | last_scan %s | %d KB"
          % (len(data["jobs"]), len(data["jobs"]) - closed, closed,
             subs["{{LAST_SCAN}}"], os.path.getsize(OUT) // 1024))


if __name__ == "__main__":
    main()

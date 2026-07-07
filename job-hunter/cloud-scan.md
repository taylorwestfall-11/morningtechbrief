# QA Job Scan — Cloud Routine Playbook

You are Taylor Westfall's QA-leadership job recruiter, running in the cloud. The repo
`https://github.com/taylorwestfall-11/morningtechbrief` is cloned at the current working
directory. Work through every step without stopping.

## Inputs (repo-relative)
- `job-hunter/config.json` — Taylor's preferences, source sites, resume profile + fit rubric.
- `job-hunter/jobs.json` — every role already found (the dedupe set; NEVER delete entries).
- `jobs-7m3k9q.html` — the published Job-tracker page. This is BOTH the live page AND the
  template you regenerate. It is search-hidden (noindex) and has a tab `<nav>` at the top.

## Targets
QA LEADERSHIP roles only: QA Manager, Senior QA Manager, QA Director / Director of QA /
Director of Quality Engineering, Head of QA, VP of Quality, plus AI-automation QE leadership
(Director of Test Automation, Head of QE, "AI-driven testing" / "LLM test automation", "QA for AI").
Primary = video game studios; secondary = QA/QE leadership at any tech/AI/SaaS company.
EXCLUDE individual-contributor roles (tester, QA/SDET engineer IC, game tester, junior analyst)
unless they carry people-management scope. Some days have ZERO new leadership roles — that is
normal; NEVER invent roles to pad the list.

## Steps
1. Read `job-hunter/config.json` and `job-hunter/jobs.json`.
2. Sweep the sources in config.json using WebSearch (date-scoped queries for the current month)
   and WebFetch on the studio career pages and boards (Hitmarker, Work With Indies, GameJobs
   Direct, RemoteGameJobs, InGameJob, LinkedIn, Indeed, Glassdoor, Built In, Wellfound,
   Levels.fyi, Dice, ZipRecruiter) — plus the games service/outsourcing vendors in
   `config.json.sources.games_service_vendors` (Side/PTW, Keywords Studios, Testronic, Virtuos,
   Lionbridge Games, Room 8 Group), whose in-house QA/localization leadership roles rarely reach
   the aggregators — and the AI-automation angle (Director of Test Automation, Head of QE,
   "AI-driven testing", "QA for AI").
3. For each candidate role capture the `config.json.job_schema` fields: title, company, category
   (games|tech), location, remote (remote|hybrid|onsite), salary, source, direct apply URL
   (prefer canonical posting over a search page), date_posted, one-line note. Leave "" if unknown.
4. Dedupe against `job-hunter/jobs.json` by `id` (lowercase-kebab `company-title`). Skip existing.
5. FIT-SCORE each NEW role against `config.json.resume.profile_for_fit` + `fit_rubric`. Add a
   `"fit"` object: `{score 0-100, level, why (1 line), blurb (2-sentence first-person
   cover-letter snippet)}`. Honor the AI bonus for AI/automation-centric roles.
6. Append new roles to `job-hunter/jobs.json` with `date_found` = today (UTC, YYYY-MM-DD).
   ALWAYS set `_meta.last_scan` to today and increment `_meta.scan_count` — even with zero new
   roles, so the page visibly shows it ran.
7. Regenerate `jobs-7m3k9q.html`: replace the JS array between the `/*__JOBS__*/` and
   `/*__JOBS_END__*/` markers with the full current jobs array from jobs.json, and set the
   `LAST_SCAN` constant to today. DO NOT modify anything else — the tab `<nav>` bar, the
   `<meta name="robots" content="noindex,nofollow">`, and the localStorage status JavaScript
   must stay byte-for-byte intact so Taylor's Applied/Dropped marks and the phone tab keep working.
8. Commit & push:
   `git add job-hunter/jobs.json jobs-7m3k9q.html`
   `git commit -m "Job scan: $(date -u +%Y-%m-%d)"`
   `git push origin HEAD`
   If the push fails, report the exact error in your final message.
9. Final message: number of new roles, which companies, top fit scores, and confirm the push.

# Job Hunter — build me my own job tracker

**How to use this:** hand this file to your AI coding agent (Claude Code, Cursor, Copilot agent — whatever you use) and say:

> Read START.md end to end, then set me up.

It works for any role — engineering, design, sales, marketing, QA. Nothing here assumes an industry.

**What you get:** a page on your phone that a robot keeps current. Every day it finds new postings matching your profile, scores each against your resume, removes the dead ones, and republishes. You mark roles applied / interviewing / rejected; that state syncs off-device so it survives your phone clearing its storage. One button copies a full job description to paste into an AI for tailoring your resume.

---

## FOR THE AI READING THIS

You are building and deploying a personal job tracker. **Read this entire file before you write anything.**

Order of work:

1. **§1** — check prerequisites
2. **§2** — interview the user. Don't skip it, don't guess their answers.
3. **§3** — read the hard-won rules. Every one is a bug that shipped in a system running in production. Do not "improve" them.
4. **§4–§8** — build
5. **§9** — deploy
6. **§10** — verify, honestly

**Copy the scripts; don't rewrite them.** §5 gives raw URLs to real, tested files. Fetch them verbatim. They encode counter-intuitive rules validated against 46 live postings — a plausible-looking reimplementation will silently reintroduce a known bug. You generate the *config*; the machinery is copied.

**Hard rule — never touch the user's access token.** Don't ask for it, read it, echo it, write it to a file, or paste it into a shell. At §9.3 you stop and hand them instructions to create it themselves and paste it into the dashboard in their browser. It must never enter this chat, the repo, or shell history.

---

## §0 — Shape of the thing

```
  DISCOVERY (AI, daily)          MAINTENANCE (scripts in CI: no AI, no API key, cannot be skipped)
  ├─ search sources              ├─ enrich.py          pasted URLs -> real entries
  ├─ score fit vs resume         ├─ deadlink_check.py  kill dead postings
  └─ append to jobs.json         ├─ postings.py        cache description text
        │                        └─ build_page.py      render the page
        └──────────────┬───────────────┘
                       ▼
              GitHub Pages (public repo) ──► phone ◄──► status.json (PRIVATE repo)
```

The organizing principle, which everything below follows from:

> **The AI does only what needs judgment — finding roles, scoring fit. Everything mechanical is a script that CI runs and nobody can skip.**

---

## §1 — Prerequisites

Check and report anything missing:

- `git`, and `gh` (GitHub CLI) authenticated — `gh auth status`
- `curl` — ships with Windows 10+, macOS, Linux
- `python3` (3.9+)
- `node` — optional but wanted; `build_page.py` uses it to syntax-check the page

**No `pip install`.** Everything is Python stdlib + `curl`. Deliberate: the scripts run in CI and on a laptop with zero setup, and a dependency that fails to install silently is a dead system.

---

## §2 — Interview the user

Ask in **2–3 batched messages**, not one at a time. Suggest defaults. All of it lands in `config.json`.

**The search**
1. What role are you hunting?
2. Which exact job titles should match? Which should be **excluded**? — *exclusions matter more than people expect; "Manager" alone returns the world.*
3. Seniority floor — what's too junior to show you?
4. Which industries? Any hard noes?
5. Where — city, remote, hybrid? Open to relocating?
6. Minimum comp, if you want to filter on it? (optional)

**Them**
7. Point me at your resume (file path), or paste it. — *You'll distill this into `profile_for_fit` (§6). Insist on a real resume; a one-line summary produces useless fit scores.*
8. Anything a resume won't show — a differentiator, a pivot you're making, something to weight heavily?

**The setup**
9. GitHub username?
10. What time should it run, and in what timezone?
11. Automation tier — read them §9.4 and let them choose.

Then **echo back a summary and get confirmation** before building.

---

## §3 — The rules

Each of these is a bug that shipped. They look like details. They are the design.

### 3.1 — An AI prompt is not an execution guarantee
The dead-link step once lived in the daily prompt marked *"MANDATORY — do not skip."* Over four consecutive days the routine ran, added 13 roles, and skipped the script every time. Nobody noticed. **Anything deterministic runs in CI where skipping is impossible.** Never put a script invocation in a prompt and call it done.

### 3.2 — Job boards lie about death. Read the body.
Aggregators return **HTTP 200, at the original URL, with the original `<title>`**, and a body reading *"Sorry, this job was removed at 10:20 a.m."* A status-code check calls that alive. **11 of 13 dead postings were exactly this.** Status-code-only checking misses ~85% of real deaths.

### 3.3 — Do NOT add an "apply affordance" guard
The obvious safety valve — *"only call it dead if the page doesn't also say Apply Now"* — was tested and **fails**: removed-job pages still render "Apply Now" in the nav and in adjacent listings, so the guard spares **9 of 11 real deaths**. The phrase list needs no guard; it fired on **0 of 46 live postings**. This is the first "fix" everyone reaches for.

### 3.4 — Never auto-close a bot-blocked posting
403/429 means blocked, not dead — and *repeated* blocks aren't evidence either; they mean the host always blocks that IP. Measured: the same sweep saw **4× 403 from a home IP and 14× from a CI runner**, including live roles at major employers. An "auto-close after N failures" rule would have deleted live jobs off the board within a week. **Close only on positive evidence.** Unverifiable roles get a badge and the human is the final oracle.

### 3.5 — Never delete or renumber a job id
`jobs.json` is append-only. Ids are the keys the user's status is stored under. Rename one and you silently orphan their "I applied to this." Dead jobs get `"closed": true`, never removal.

### 3.6 — Losing local state must never erase a tracked job
The nastiest one. Rule A: *hide dead postings*. Rule B: *status lives in localStorage*. Both sensible. Together: the phone cleared storage → applied roles reverted to `new` → they were also `closed:true` → and so **vanished from every view and every count**, silently, including two the user had really applied to.

> **A job that has ever left `new` is never auto-hidden, for any reason.**

Implement it as an invariant that does not depend on sync working (§7.2).

### 3.7 — …but the invariant needs an escape hatch
It reads the status record to decide. When the record itself is *lost* — the actual bug — a dead posting you'd applied to fails the check and hides everywhere, and then **can't be re-marked because it can't be seen**. The roles most worth recovering were the ones made unreachable. **Ship an archive view** that reveals dead *and dismissed* roles so one can be set back (§7.1).

### 3.8 — Use `curl`, not `urllib`
Tested: `urllib` fails outright on postings `curl` fetches fine — real job sites are picky about TLS and redirects in ways `curl` and browsers handle. `curl` ships everywhere, including CI. It looks like a dependency worth removing. It isn't.

### 3.9 — Drag-and-drop does not work on phones
HTML5 DnD (`draggable`, `ondragstart`) **never fires from touch on Android Chrome** and is unusable on iOS Safari. A kanban built on it means a job can be moved *into* Applied and then never moved again — decoratively interactive, functionally read-only. **Every card gets a tappable stage control.** Drag is optional desktop garnish.

### 3.10 — The AI must never hand-edit the published page
Rendering is `build_page.py`'s job. The original had the model regenerate a 115KB page daily, editing around markers while keeping the state-handling JavaScript "byte-for-byte intact." That's a corruption waiting to happen, and it silently reformatted the file at least once.

### 3.11 — Scraped text that looks like success
Scraping a JS-rendered posting with `curl` returns the careers **index** — nav, filters, every open role — and it's several KB, so length reads as success. Three roles each cached 18,481 identical chars of *"Open Positions: 156 | Select a Craft | Accounting Admin Art…"*. **Junk is worse than nothing here**: the text feeds an AI tailoring a resume, and an index would poison it silently. Anything scraped must prove it's a job description.

### 3.12 — Unescape before stripping tags
Greenhouse's `content` is HTML-*escaped* HTML. Strip tags first and the regex matches nothing; the later unescape then **creates** the tags. 187 leaked into one cached posting.

### 3.13 — Python text mode writes CRLF on Windows
It broke a separator match and duplicated a header into every copied posting. Use `newline="\n"` for anything a browser will parse.

### 3.14 — 16px minimum on anything focusable
iOS Safari zooms the whole page in on focus for any `input`, `textarea` **or `select`** under 16px, and won't zoom back cleanly. Android doesn't, but the rule costs nothing.

### 3.15 — Measure the layout; don't eyeball it
A nav and a counts row were silently **wrapping to two rows** on a 393px phone — chrome ate **48% of the screen** before the first job. Nothing in the code says "I wrapped." Measure `getBoundingClientRect()` at a real phone width.

### 3.16 — A page can render and still be dead
One duplicated `let` in a shared scope killed an entire script: markup rendered, **zero jobs, no console error**. It looked like empty data, not a crash — and string-presence assertions passed it happily. `build_page.py` runs `node --check` on the page's JS and refuses to write when it doesn't parse. Keep that.

---

## §4 — Repo layout

Use this layout exactly — the scripts in §5 expect it and then need no edits.

```
<user>/job-hunter/                PUBLIC repo (GitHub Pages serves it)
├─ job-hunter/
│  ├─ config.json                 you generate this (§6)
│  ├─ jobs.json                   append-only catalog
│  ├─ inbox.json                  {"items":[]} — URLs pasted from the phone
│  ├─ deadlink_check.py           §5, verbatim
│  ├─ enrich.py                   §5, verbatim
│  ├─ postings.py                 §5, verbatim
│  ├─ build_page.py               §5, verbatim
│  ├─ postings/                   cached description text (created automatically)
│  ├─ template/dashboard.html     §5, verbatim
│  └─ scan.md                     you generate this (§8)
├─ .github/workflows/maintain-jobs.yml   §5, verbatim
├─ manifest.json  icon-192.png  icon-512.png            §5
└─ index.html                     generated — never hand-edit

<user>/job-hunter-state/          PRIVATE repo — see §4.1
└─ status.json                    {"_meta":{"version":1},"jobs":{}}
```

### §4.1 — Why two repos

`status.json` holds which roles they applied to, recruiter names, comp discussions, interview dates, private notes. **That is their live job search.** In a public repo under their real name, their current employer can find it — and once pushed, git history, forks and caches make it effectively permanent.

GitHub Pages won't serve a private repo without a paid plan, so split by sensitivity:

- **public** `job-hunter` — the page, the listings, the inbox. Nothing sensitive.
- **private** `job-hunter-state` — `status.json` and nothing else.

One fine-grained token covers both. No workflow ever reads the private repo, so this costs nothing in complexity. **Tell the user why** — don't silently create two repos.

---

## §5 — Fetch the machinery (do not rewrite)

These are live, tested files. Fetch each and commit it at the path shown. Base:

```
https://raw.githubusercontent.com/taylorwestfall-11/morningtechbrief/main/
```

| Fetch from | Save as |
|---|---|
| `job-hunter/deadlink_check.py` | `job-hunter/deadlink_check.py` |
| `job-hunter/enrich.py` | `job-hunter/enrich.py` |
| `job-hunter/postings.py` | `job-hunter/postings.py` |
| `job-hunter/build_page.py` | `job-hunter/build_page.py` |
| `job-hunter/template/dashboard.html` | `job-hunter/template/dashboard.html` |
| `.github/workflows/maintain-jobs.yml` | `.github/workflows/maintain-jobs.yml` |
| `manifest.json` | `manifest.json` |
| `icon-192.png`, `icon-512.png` | repo root |

```bash
B=https://raw.githubusercontent.com/taylorwestfall-11/morningtechbrief/main
mkdir -p job-hunter/template .github/workflows
for f in deadlink_check.py enrich.py postings.py build_page.py; do
  curl -fsSL "$B/job-hunter/$f" -o "job-hunter/$f"; done
curl -fsSL "$B/job-hunter/template/dashboard.html" -o job-hunter/template/dashboard.html
curl -fsSL "$B/.github/workflows/maintain-jobs.yml" -o .github/workflows/maintain-jobs.yml
curl -fsSL "$B/manifest.json" -o manifest.json
curl -fsSL "$B/icon-192.png" -o icon-192.png
curl -fsSL "$B/icon-512.png" -o icon-512.png
```

**Then adapt exactly these, and nothing else:**

1. `manifest.json` — set `start_url` and `scope` to `/<repo-name>/`. Scope is what stops a tab tap kicking iOS out to an in-app browser with a URL bar.
2. `job-hunter/template/dashboard.html` — the `<head>` hardcodes `/morningtechbrief/` in the manifest and icon links. Point them at your repo.
3. `.github/workflows/maintain-jobs.yml` — the commit step names `jobs-7m3k9q.html`; change it to your `branding.page` (§6).
4. Seed `job-hunter/inbox.json` with `{"items":[]}` and `job-hunter/jobs.json` with `{"_meta":{"last_scan":"","scan_count":0},"jobs":[]}`.

**Re-fetch these files occasionally.** The dead-link ruleset is a living thing — aggregators change their "removed" wording, new soft-404 phrasings appear. That's the one real cost of copying instead of forking: nothing tells you when a rule improves.

---

## §6 — `config.json`

Generate from the interview. Nothing here is role-specific.

```jsonc
{
  "candidate": {
    "name": "", "email": "", "location_preference": "",
    "seniority_floor": "",
    "target_titles": [], "exclude_titles": [],
    "scope": "one line: what you're hunting and where"
  },
  "resume": { "profile_for_fit": "", "fit_rubric": "" },
  "sources": { "<your group name>": [ { "name": "", "url": "" } ] },
  "repos": { "public": "<user>/job-hunter", "state": "<user>/job-hunter-state" },
  "branding": {
    "title": "Job Tracker",
    "emoji": "💼",
    "page": "index.html",
    "brand": "",
    "nav": []
  },
  "job_schema": {
    "fields": ["id","title","company","category","location","remote","salary",
               "source","url","date_found","date_posted","notes","closed"]
  }
}
```

**`profile_for_fit`** — one dense paragraph distilled from their actual resume: level, years, current and notable past employers, core strengths, credentials, and the differentiator from question 8. It is the single input to every fit score; a vague one makes the whole system useless.

**`fit_rubric`** — what each band *means for this person*, in their domain:

> Score 0–100. **Excellent (90–100):** [their ideal — right industry, level, specialty]. **Strong (80–89):** [right industry, slightly off level]. **Good (65–79):** [adjacent industry or under-levelled]. **Stretch (50–64):** [a real reach or a domain change]. **Low (<50):** [wrong field or scope]. **Bonus:** +5 to +10 when a posting centres on [their differentiator]. Output a one-line `why` and a two-sentence first-person `blurb`.

**`sources`** — build with the user. Ask where people in *their* field actually post. Include the big aggregators, 2–3 niche boards for their industry, and **direct careers pages for 15–25 target employers**. The niche and direct sources produce the best roles; the big aggregators produce most of the dead links.

**`branding.nav`** — leave `[]` for a single page and no bar renders. Only populate it if you're linking sibling pages, in which case every page's bar must stay pixel-identical or the top of the screen visibly reflows when switching.

---

## §7 — The dashboard

`template/dashboard.html` is fetched, not written. It's one self-contained file: no build step, no framework, no CDN. `build_page.py` fills `{{TITLE}}`, `{{EMOJI}}`, `{{NAV}}`, `{{STATE_REPO}}`, `{{PUBLIC_REPO}}`, `{{LAST_SCAN}}` and the jobs array.

Restyle it freely — but if you touch behaviour, these are load-bearing:

### §7.1 — What it must keep doing
- **A tappable stage control on every card** (§3.9). A `<select>` is genuinely best here — native wheel on iOS, native dropdown on Android, free.
- **An archive view** revealing dead **and dismissed** roles (§3.7). The list normally renders the `home` group only; the archive must also show the `dismissed` group, or it reveals dead postings but not the role just mis-tapped — the entire reason someone opens it.
- **Undo** after a stage change. Dismissing is one tap and hides a role everywhere; recovery shouldn't be archaeology.
- **Copy job posting** — fetches `job-hunter/postings/<id>.txt` same-origin, falls back to details + URL.
- Search + one filter button opening a bottom sheet. Tap targets ≥44px. 16px fonts (§3.14).
- Badges: `🔗 posting closed`, `⚠️ unverified`, `✨ new`, posted date.
- `<meta name="robots" content="noindex,nofollow">` + a robots.txt disallow. It's link-public; keep it out of search.

### §7.2 — The invariant (verbatim)

```js
// A job that has EVER left "new" is never auto-hidden. Not when its posting
// dies, not when sync fails, not when the phone wipes its storage. This is the
// bug that made two real applications silently disappear.
const everEngaged = (id) => {
  const r = state.jobs[id];
  return !!r && (r.status !== "new" || (r.history && r.history.length) || !!r.notes);
};
const isHidden = (job) =>
  filters.archive ? false                       // the escape hatch — see §3.7
  : statusOf(job.id) === "not-interested" || (job.closed && !everEngaged(job.id));
```

### §7.3 — Sync

`status.json` in the **private** repo:

```jsonc
{
  "_meta": { "version": 1, "updated_at": "2026-07-15T18:22:10Z" },
  "jobs": {
    "<job-id>": {
      "status": "applied", "date": "2026-07-05",
      "notes": "Recruiter: Dana. Onsite 7/22.",
      "updated_at": "2026-07-05T18:22:10Z",
      "history": [ { "status": "applied", "at": "2026-07-05T18:22:10Z" } ]
    }
  }
}
```

- **localStorage is a cache, never the record.** Write it first so the UI never lags, then sync.
- **On load:** render from cache instantly → fetch remote → **merge** → re-render. Last-write-wins per job on `updated_at`.
- **Merge, never replace.** A fetch must never clear local state. Remote empty + local full → local wins and pushes.
- **On change:** write local → debounce ~2s → `PUT` via the GitHub Contents API with the `sha`. On 409, refetch, merge, retry.
- **No token:** works fully, locally. Show a persistent "not syncing — this device only" banner. Don't nag beyond that.
- Call `navigator.storage.persist()` and ship a manifest. Android honours it and largely stops evicting; iOS partially.
- **Why:** iOS Safari evicts local storage on its own schedule, and a home-screen web app can keep a *separate* store from Safari. "It worked yesterday" is not evidence it persists.

---

## §8 — `job-hunter/scan.md`

Generate from the interview — the instruction sheet the daily AI run follows. It must say:

1. Read `job-hunter/config.json` and `job-hunter/jobs.json`.
2. Search `config.sources` for roles matching `target_titles`, honouring `exclude_titles` and `seniority_floor`. Date-scope to the last few days.
3. For each candidate capture: `id` (kebab `company-title`), `title`, `company`, `category`, `location`, `remote`, `salary`, `source`, `url`, `date_posted`, `notes`. Unknowns stay `""` — **never guess a date**.
4. **Prefer the employer's own ATS link** (Greenhouse, Lever, Workable, Ashby) over an aggregator. Aggregators are where links rot (§3.2), *and* ATS APIs give clean description text and never bot-block, so an ATS link is worth more twice over. Follow an aggregator's Apply button to the real posting.
5. **Require a direct posting URL.** Never add a role whose only link is a search page or a careers root.
6. Dedupe on `id` **and** near-duplicates: same company, titles matching after lowercasing, stripping parentheticals, dropping senior/sr/lead/staff/principal. **Never renumber an existing id** (§3.5).
7. Fit-score each new role against `config.resume`. Add `fit: {score, level, why, blurb}`.
8. Append with `date_found` = today and `"closed": false`. Always set `_meta.last_scan` to today, even on a zero-role day, so the page proves it ran.
9. **Commit only `job-hunter/jobs.json`, then stop.** Don't check links, don't build the page, don't touch the HTML — CI owns all of it (§3.1, §3.10). The push triggers it.
10. Some days there are no new roles. That's normal. **Never invent one to pad the list.**

---

## §9 — Deploy

### §9.1 Repos
```bash
gh repo create job-hunter       --public  --clone
gh repo create job-hunter-state --private --clone
```
Seed the private one with `{"_meta":{"version":1},"jobs":{}}` in `status.json`.

### §9.2 Pages
Enable Pages on the public repo, branch `main`, root. **Two gotchas that fail silently:**

- The repo's **default workflow token is read-only**. The workflow declares `contents: write` explicitly — keep that.
- Branch-based ("legacy") Pages does **not** reliably rebuild on a push made with `GITHUB_TOKEN`. The workflow POSTs `repos/{owner}/{repo}/pages/builds` with `pages: write` to force it. Without that the sweep runs, logs success, commits correctly — and the phone shows a stale board. A green check that lies.
- Editing anything under `.github/workflows/` needs the **`workflow` scope** on the gh token: `gh auth refresh -h github.com -s workflow`.

### §9.3 The token — STOP AND HAND OFF

Don't do this for them. Print this and let them do it, **on the phone they'll use** — the token is shown once, and creating it on a desktop means moving a secret to the phone somehow:

> 1. **github.com → Settings → Developer settings → Personal access tokens → Fine-grained → Generate new token**
> 2. **Repository access → Only select repositories** → pick **both** `job-hunter` and `job-hunter-state`
> 3. **Permissions → Repository permissions → Contents → Read and write.** Nothing else. *(Metadata: Read-only is added automatically — that's expected.)*
> 4. Set an expiry you're happy with. Sync dies silently the day it lapses.
> 5. Copy it, open your board, tap the sync chip, paste.
>
> Don't paste it into this chat, a file, or a terminal. It belongs only in the dashboard. Revoke it anytime.

**Troubleshooting, because GitHub's error is misleading:** a fine-grained token returns **404, not 403**, for a repo it can't see. So "Sync error 404" almost always means the private repo wasn't ticked in step 2 — not a missing file. 403 means Contents isn't set to Read *and write*.

### §9.4 Automation tier — let them choose

The deterministic core needs **no LLM and no secrets**, so this degrades gracefully:

| Tier | Discovery | Maintenance | Cost |
|---|---|---|---|
| **0** | none — add jobs by pasting links | Actions, daily | free |
| **1** | on demand: *"run my scan"* to your own AI, following `job-hunter/scan.md` | Actions, daily | free |
| **2** | Actions + an `ANTHROPIC_API_KEY` secret running `scan.md` | Actions, daily | API usage |
| **3** | a scheduled cloud agent on an AI subscription | Actions, daily | subscription |

Maintenance is identical in every tier — that's the point. **Tier 1 is the right default:** free, and the board still maintains itself.

---

## §10 — Verify

Don't skip, and don't report success you haven't seen:

1. `python job-hunter/deadlink_check.py` — prints a summary line.
2. `python job-hunter/postings.py` — caches description text. Expect roughly a third to fail; JS-rendered and bot-blocked sites have no usable text and that's handled.
3. `python job-hunter/build_page.py` — writes the page. **If the JS doesn't parse it refuses to write** (§3.16).
4. `gh workflow run "Maintain job board"` → confirm green.
5. **Open it on the user's actual phone.** Mark a role applied, force-quit the browser, reopen — it must survive. Then move it to Interview. If either fails, §3.6 or §3.9 is broken. Fix before calling this done.
6. Confirm `status.json` in the private repo picked up the change.

**Expect a caching lag.** Pages deploys in 30–60s, then `Cache-Control: max-age=600` holds the old copy for up to 10 more minutes. Home-screen web apps cache harder still — deleting and re-adding the icon clears it, and is needed anyway for the manifest to apply.

---

## §11 — Report back

Tell the user, plainly:

- their board URL, and that it's link-public but hidden from search;
- that their notes and statuses are in the **private** repo, and why that matters;
- which tier they're on and what runs when;
- how many sources are swept — and to tell you when a good role comes from somewhere not on the list;
- that dead-link rules go stale as boards change their wording. When a dead posting survives, add its phrase to `DECISIVE` in `deadlink_check.py` — or re-fetch the file (§5) and pick up the current ruleset.

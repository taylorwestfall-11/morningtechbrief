# Taylor's Daily Routine — Morning Brief + Job Scan

You are running Taylor Westfall's combined daily routine. Work through **all parts completely without stopping**.
All files are in the current working directory (the cloned repo root).

---

## PART 1 — Morning Tech Brief

### Step 1 — Load preferences
Read `brief_prompt.txt` for any topic/source priorities. Ignore the Windows file paths in that file — use the repo-relative paths below instead.

### Step 2 — Search for today's news
Run multiple web searches for stories published in the **last 24 hours** across:
- **AI & ML**: Anthropic blog, OpenAI blog, Hugging Face, Google DeepMind, VentureBeat AI
- **Hardware**: Tom's Hardware, Ars Technica, AnandTech
- **General Tech**: The Verge, Wired, Hacker News, Gizmodo
- **Home Automation**: Home Assistant blog, smart home / IoT news
- **Creative & Motion**: Motionographer, motion design news

### Step 3 — Regenerate `morning_brief.html`
Read the current `morning_brief.html` for the exact CSS and layout — do not change any styling.
Taylor's profile: tech tinkerer, digital animation background, active home automation projects,
understands tech patterns without being a developer. Prioritize stories connecting to home
automation, creative tech, and practical AI tools.

Overwrite `morning_brief.html` with the full updated page:
- Update the date in the header to today's date (UTC).
- Replace all story content with today's news.
- Keep all sections: Top Picks (4 cards), AI & ML, Hardware, Home Automation, Creative & Motion, Quick Hits, Feedback footer.
- Keep all vote/feedback JavaScript intact.
- **IMPORTANT**: Keep the `<nav>` block at the top of `<body>` byte-for-byte — it links "📰 AI News" and "💼 Jobs" and must not change.
- Every story preview/excerpt (`<p>` inside `.pick-card` and `.story-body`) must be **≤ 50 words**. Trim to the first ~50 words; end on a complete sentence where possible.

### Step 4 — Update the archive
Append today's top 5 stories as plain text to `tech_news_archive.md`.
Format: `## [Date]` followed by a short bullet list.

---

## PART 2 — QA Leadership Job Scan

Read `job-hunter/cloud-scan.md` and follow **every step in that file exactly**, with one change:
**skip its Step 8 git commit/push** — the commit is handled at the end of this routine (below).

---

## PART 3 — Commit & Push Everything

Stage and commit all changed files in one commit:

```
git add morning_brief.html tech_news_archive.md job-hunter/jobs.json jobs-7m3k9q.html
git commit -m "Daily routine: $(date -u +%Y-%m-%d)"
git push origin HEAD
```

If the push is rejected (remote has new commits), run `git pull --rebase origin HEAD` then push again.
Report the final push status.

---

## PART 4 — Notify

Send a PushNotification summarising:
- Top 2–3 news stories from Part 1
- New job roles found in Part 2 (company, title, fit score), or "no new roles today"
- Any dead links newly closed
- Confirm the push succeeded (or report the error)

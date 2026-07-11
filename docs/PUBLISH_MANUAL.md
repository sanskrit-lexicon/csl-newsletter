# csl-newsletter Publish Manual

_Created: 11-07-2026 · Last updated: 11-07-2026_

The operator manual for compiling and publishing a monthly (or annual) CDSL
newsletter edition: generate the activity draft, edit it into prose, commit
the edition file, mirror it to the csl-guides blog, and — once the delivery
channel is live — send it to subscribers. This is the **human-runnable
fallback**; the `/cdsl-newsletter-publisher` workflow skill encodes the same
steps for agent runs. The two must not drift: a step changed here changes
there.

Companion metadoc: [docs/PUBLISH_MANUAL.meta.md](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/docs/PUBLISH_MANUAL.meta.md).

---

## 1. Cheat-sheet — one monthly edition, end to end

```sh
# 0. prerequisites: gh auth login (once); a csl-guides clone beside this repo

# 1. generate the raw activity draft for an EXPLICIT window (never open-ended)
python scripts/draft-newsletter.py --since 2026-07-01 --until 2026-07-31 --output draft.md

# 2. EDIT draft.md — the human step: replace the commit/issue log with
#    3–5 prose highlights (warm tone, readable by Sanskrit scholars)

# 3. commit the edition + archive-index row
cp draft.md july2026.md
#   add the new row at the TOP of readme.md's monthly table
git add july2026.md readme.md
git commit -m "newsletter: add july 2026 edition"

# 4. mirror to the blog (sibling csl-guides repo)
#    csl-guides/blog/2026-07-31-cdsl-newsletter-2026-07.md
#    Docusaurus frontmatter + <!-- truncate -->; june2026 post = template
#    validate: npm run build   (in csl-guides)

# 5. send — ⛔ NOT YET LIVE: the delivery channel (Buttondown vs a
#    reply-to-list) is an open MG decision; editions stop at the blog for now
```

## 2. Data-flow diagram

```
GitHub org activity  (every active sanskrit-lexicon repo)
│   commits + closed issues over --since/--until, bots filtered
│   (github-actions, dependabot, web-flow)
▼  scripts/draft-newsletter.py   (gh api, paginated; requires gh auth)
draft.md   = Docusaurus-ready frontmatter + a structured ACTIVITY LOG
│              with editing instructions baked in
▼  HUMAN EDIT — the log is raw material, never the newsletter:
│    pick 3–5 highlights, write prose, keep the email skeleton
│    (Date:/Subject: header · greeting · sections · footer links ·
│     unsubscribe line — see any shipped edition)
├──► {month}{year}.md   THIS repo — the email/archive file  [COMMITTED]
│       + a new top row in readme.md's monthly table
├──► csl-guides/blog/YYYY-MM-DD-cdsl-newsletter-YYYY-MM.md
│       the public post (same prose, no email header)
│       → renders at sanskrit-lexicon.github.io/csl-guides/news
└──► (pending) email send — Buttondown account NOT yet created;
        subscribe page staged at csl-guides/users/newsletter
```

Annual editions (`annual{YYYY}.md`) follow the same flow with a year window
and the `newsletter-YYYY-annual` blog slug.

## 3. Step-by-step operator walkthrough

### 3.1 Generate the draft

```sh
python scripts/draft-newsletter.py --since YYYY-MM-01 --until YYYY-MM-DD --output draft.md
```

[scripts/draft-newsletter.py](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/scripts/draft-newsletter.py)
walks every active repo in the `sanskrit-lexicon` org via `gh api`
(paginated), collects commits and closed issues in the window, filters bot
authors, and writes a structured draft: blog frontmatter + per-repo activity
log + inline editing instructions. **Always pass an explicit window** —
month = first→last day; default (no flags) is "last 30 days", which drifts
against calendar months. No flags → stdout; `--output` → file.

### 3.2 Edit into prose — the step no script does

The activity log is source material. The shipped edition is 3–5 **prose
highlights** in a warm register accessible to Sanskrit scholars (not a
commit digest). Keep the email skeleton every shipped edition uses
(template: [june2026.md](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/june2026.md)):

```
Date: {Day}, {DD} {Mon} {YYYY}
Subject: Cologne Sanskrit Dictionaries update ({Month} {YYYY})

Dear Sanskrit scholars, students, and dictionary enthusiasts,
…intro… …named sections, one per highlight…
------------------------------------------------------------
Useful links: …standard footer…
To unsubscribe from future updates, reply with "unsubscribe" in the subject line.
```

### 3.3 Commit the edition + archive row

Naming: `{month}{year}.md` all-lowercase (`july2026.md`); annuals
`annual{YYYY}.md`. Add the new row **at the top** of the right
[readme.md](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/readme.md)
archive table (most-recent-first), with the correct status word — the
August–December 2026 files are pre-created **templates**, so when you fill
one, flip its status from `template` to `drafted`/sent. Commit both files
together.

### 3.4 Mirror to the csl-guides blog

Create `csl-guides/blog/YYYY-MM-DD-cdsl-newsletter-YYYY-MM.md` (date = the
edition date): the same prose without the email header, Docusaurus
frontmatter (slug, title, date, `newsletter` tag — slugs stay distinct
between monthly and annual), and `<!-- truncate -->` after the intro. Use
the existing june2026 post as the literal template. Validate with
`npm run build` in csl-guides before merging; posts render at
[/news](https://sanskrit-lexicon.github.io/csl-guides/news). The blog and
the archive **always move together** — an edition in one repo without its
twin is a defect.

### 3.5 Send — the pending step

**The delivery channel is not live** (state of 11-07-2026, per the
[readme](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/readme.md)):
the intended tool is Buttondown, but the account is not created and
Buttondown-vs-reply-to-list (Groups.io) is an open MG decision. None of the
2026 editions has been mailed. When the channel goes live: paste the
`{month}{year}.md` content (it is already plain-text email), send, and
record the send date. NB
[CLAUDE.md](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/CLAUDE.md)
still states Buttondown as operational — the readme is the current truth
(§5, row 1).

## 4. Environment & prerequisites

- **Python 3** + the **`gh` CLI, authenticated** (`gh auth login`) — the
  draft generator is stdlib-only otherwise.
- A **csl-guides clone** (sibling directory) with `npm install` done, for
  the blog mirror + build check.
- No secrets in this repo. A future Buttondown key would live outside git
  (org convention: `~/.secrets/`).

## 5. Symptom → cause → cure

| Symptom | Cause | Cure |
|---|---|---|
| CLAUDE.md says "delivery via Buttondown", readme says not live | CLAUDE.md predates the H549 readme refresh; the channel decision is still open | Trust the readme; treat §3.5 as pending until the MG decision lands (then update BOTH files + this manual) |
| Draft covers the wrong days | Ran without `--since/--until` — default is rolling 30 days, not the calendar month | Always pass the explicit window (§3.1) |
| Draft missing a repo's activity | `gh` unauthenticated (silent `None`/empty on API failure), or the repo had bots only | `gh auth status`; rerun; check the repo's commits by hand if suspicious — the script swallows per-repo API errors silently |
| Edition reads like a commit log | §3.2 skipped | The log is raw material; write the 3–5 highlights — this is the one step that cannot be automated away |
| Blog post missing while the email file exists (or vice versa) | The two-repo sync rule broken | Create the twin now (§3.4); the pairing is the core invariant |
| Docusaurus build fails on the new post | Frontmatter (slug collision, bad date) or missing `<!-- truncate -->` | Copy the june2026 post's frontmatter shape exactly; slugs distinct monthly vs annual |
| New edition not in the readme table / status still `template` | §3.3 half-done | Top row, most-recent-first, correct status word |
| Tempted to hand-edit an August–December 2026 file "later" | They are placeholder templates awaiting content | Fill via the full workflow when the month arrives; don't ship a skeleton |
| Subscribers ask why nothing arrives | No sends yet — channel pending | Point to the blog + the staged subscribe page; the send step starts at channel go-live |

## 6. Glossary

| Term | Meaning |
|---|---|
| edition | One `{month}{year}.md` (or `annual{YYYY}.md`) — plain-text email content in Markdown, the archival unit |
| activity log | draft-newsletter.py's raw per-repo commit/issue listing — input to editing, never shipped as-is |
| highlight | One prose section of the shipped edition (3–5 per month) |
| the pairing | The invariant that every edition exists twice: archive file here + blog post in csl-guides |
| Buttondown | The intended (not yet live) email-delivery service |
| template edition | A pre-created future-month skeleton (Aug–Dec 2026), status `template` in the readme table |
| `<!-- truncate -->` | Docusaurus blog marker splitting the preview from the full post |
| annual | The year-in-review edition (`annualYYYY.md`, series since 2014) |

## 7. Maintainer appendix

- **Invariants:** explicit date windows; the two-repo pairing; readme table
  most-recent-first with true status; the email skeleton (subject format,
  footer, unsubscribe line) stable across editions; prose highlights, never
  raw logs.
- **Automation vs manual:** `/cdsl-newsletter-publisher` (a workflow skill,
  mirrored to Codex) runs §3.1–§3.4 with the same rules and stops for human
  prose selection; this manual is the fallback and the specification. Change
  the process → update skill + manual together.
- **Observed quirks** (11-07-2026, while writing this manual): (1) the
  CLAUDE.md/readme Buttondown contradiction (§5 row 1) — CLAUDE.md needs a
  correction once the channel decision lands (or now, to "planned");
  (2) draft-newsletter.py swallows per-repo `gh api` failures silently
  (returns `None`/`[]`) — a partially-authenticated run produces a
  plausible-looking but incomplete draft; (3) the readme's archive tables
  are hand-maintained — nothing checks a committed edition actually has its
  row (or its blog twin).
- **History:** monthly series 2021–2023, revived 2026; annuals since 2014.
  The 2026 revival's first two editions (june, july) are drafted; delivery
  awaits the channel decision.
- **Issue taxonomy:** tooling-repo taxonomy — see
  [CLAUDE.md](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/CLAUDE.md).

---

_Dr. Mārcis Gasūns_

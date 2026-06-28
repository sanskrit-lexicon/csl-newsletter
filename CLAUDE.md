# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with this repository.

## What this is

**csl-newsletter** is the archive and tooling home for the monthly Cologne Digital Sanskrit
Dictionaries email newsletter. Each edition is stored as `{month}{year}.md` (e.g.
`june2026.md`) — the plain-text email content, exactly as sent.

Past editions are also published as blog posts on the guides site at
https://sanskrit-lexicon.github.io/csl-guides/news

Email delivery is handled via **Buttondown** (https://buttondown.com/cdsl).
Replace `cdsl` with the actual account username if it differs.

## Monthly workflow

```sh
# 1. Generate a raw draft from the past 30 days of org activity
python scripts/draft-newsletter.py --output draft.md

# 2. Edit draft.md — replace the commit/issue log with 3–5 prose highlights.
#    Warm tone; accessible to Sanskrit scholars, not just developers.

# 3. Commit the finished edition to this repo
cp draft.md {month}{year}.md    # e.g. july2026.md
git add {month}{year}.md readme.md
git commit -m "newsletter: add {month} {year} edition"

# 4. Also commit a blog post to csl-guides
#    Copy the prose (without the email header) to:
#    csl-guides/blog/YYYY-MM-DD-cdsl-newsletter-YYYY-MM.md
#    with Docusaurus frontmatter (see june2026 post as the template).

# 5. Send via Buttondown — paste the .md content and send.
```

## File format

Each `{month}{year}.md` file is plain-text email content in Markdown:

```
Date: {Day}, {DD} {Mon} {YYYY}
Subject: Cologne Sanskrit Dictionaries update ({Month} {YYYY})

Dear Sanskrit scholars, students, and dictionary enthusiasts,

[intro paragraph]

[named sections — one per highlight]

------------------------------------------------------------
Useful links:
[standard footer block]

To unsubscribe from future updates, reply with "unsubscribe" in the subject line.
```

## Adding a new edition to readme.md

After committing `{month}{year}.md`, add a row to the archive table in `readme.md`:

```markdown
| {YYYY} | {Month} | [{Month}, {YYYY}](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/{month}{year}.md) |
```

Insert at the top of the table (most recent first).

## draft-newsletter.py

`scripts/draft-newsletter.py` uses the `gh` CLI to pull commits and closed issues from all
active repos in the `sanskrit-lexicon` org over the past 30 days, then outputs a structured
Markdown draft with editing instructions. Requires `gh auth login`.

```sh
python scripts/draft-newsletter.py [--since YYYY-MM-DD] [--output FILE]
```

## GitHub Issue Conventions

This repository uses the Cologne tooling-repo taxonomy. All issues must have:
- **Exactly one type label** — `bug` · `feature` · `enhancement` · `performance` ·
  `tech-debt` · `security` · `documentation` · `infrastructure` · `question`
- **Exactly one severity label** — `trivial` · `minor` · `major` · `critical`
- **One milestone** — API Stability · User Experience · Data Quality ·
  Developer Experience · Community

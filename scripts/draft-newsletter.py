#!/usr/bin/env python3
"""
Draft a monthly CDSL newsletter from GitHub activity across the org.

Reads commits and closed issues for every active repo in the last N days,
then outputs a Markdown draft ready to edit and paste into Buttondown.

Usage:
    python scripts/draft-newsletter.py
    python scripts/draft-newsletter.py --since 2026-06-01
    python scripts/draft-newsletter.py --output blog/2026-06-28-cdsl-newsletter-june-2026.md

Requires: gh CLI authenticated (`gh auth login`)
"""
import sys
import json
import subprocess
import argparse
from datetime import datetime, timedelta, timezone

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

ORG = 'sanskrit-lexicon'

BOT_AUTHORS = {'github-actions[bot]', 'dependabot[bot]', 'web-flow'}


def gh_json(path):
    result = subprocess.run(
        ['gh', 'api', path],
        capture_output=True, encoding='utf-8'
    )
    if result.returncode != 0:
        return None
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError:
        return None


def gh_paginate(path):
    result = subprocess.run(
        ['gh', 'api', '--paginate', path],
        capture_output=True, encoding='utf-8'
    )
    if result.returncode != 0:
        return []
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError:
        return []


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--since', default=None,
                        help='Start date YYYY-MM-DD (default: 30 days ago)')
    parser.add_argument('--output', '-o', default='-',
                        help='Output file path (default: stdout)')
    args = parser.parse_args()

    if args.since:
        since_dt = datetime.fromisoformat(args.since).replace(tzinfo=timezone.utc)
    else:
        since_dt = datetime.now(timezone.utc) - timedelta(days=30)

    now = datetime.now(timezone.utc)
    since_iso = since_dt.strftime('%Y-%m-%dT%H:%M:%SZ')
    month_year = now.strftime('%B %Y')
    period = f"{since_dt.strftime('%Y-%m-%d')} to {now.strftime('%Y-%m-%d')}"

    print(f"Fetching repos for {ORG}...", file=sys.stderr)
    all_repos = gh_paginate(f'/orgs/{ORG}/repos?per_page=100')
    active_repos = sorted(
        [r for r in all_repos
         if not r.get('archived') and r.get('pushed_at', '') >= since_iso],
        key=lambda r: r['pushed_at'],
        reverse=True,
    )
    print(f"  {len(active_repos)} of {len(all_repos)} repos active since {since_iso[:10]}",
          file=sys.stderr)

    repo_sections = []

    for repo in active_repos:
        name = repo['name']
        desc = repo.get('description') or ''
        print(f"  {name}", file=sys.stderr)

        commits = gh_json(
            f'/repos/{ORG}/{name}/commits?since={since_iso}&per_page=100'
        ) or []
        commits = [
            c for c in commits
            if c.get('commit', {}).get('author', {}).get('name') not in BOT_AUTHORS
            and not c.get('commit', {}).get('message', '').startswith('Merge')
        ]

        issues = gh_json(
            f'/repos/{ORG}/{name}/issues?state=closed&since={since_iso}&per_page=100'
        ) or []
        issues = [
            i for i in issues
            if 'pull_request' not in i
            and (i.get('closed_at') or '') >= since_iso
        ]

        if not commits and not issues:
            continue

        lines = [f"### [{name}](https://github.com/{ORG}/{name})"]
        if desc:
            lines.append(f"_{desc}_\n")

        if commits:
            lines.append(f"**{len(commits)} commit(s):**\n")
            for c in commits[:15]:
                msg = c['commit']['message'].split('\n')[0][:120]
                sha = c['sha'][:7]
                url = c['html_url']
                date = c['commit']['author']['date'][:10]
                lines.append(f"- [`{sha}`]({url}) `{date}` {msg}")
            if len(commits) > 15:
                lines.append(f"- _…and {len(commits) - 15} more_")

        if issues:
            lines.append(f"\n**{len(issues)} issue(s) closed:**\n")
            for i in issues[:15]:
                lines.append(f"- [#{i['number']}]({i['html_url']}) {i['title']}")
            if len(issues) > 15:
                lines.append(f"- _…and {len(issues) - 15} more_")

        repo_sections.append('\n'.join(lines))

    activity_block = (
        '\n\n---\n\n'.join(repo_sections)
        if repo_sections
        else '_No repository activity found for this period._'
    )

    slug = f"newsletter-{now.strftime('%Y-%m')}"
    file_date = now.strftime('%Y-%m-%d')

    draft = f"""---
slug: {slug}
title: "CDSL Newsletter — {month_year}"
authors: []
tags: [newsletter]
date: {file_date}
---

<!--
  DRAFT — edit before sending.
  Generated: {file_date}  ·  Period: {period}

  Editing steps:
  1. Replace the raw activity log with 3–5 named prose highlights.
  2. Warm tone — accessible to scholars, not just a commit log.
  3. Commit this file to:
       blog/{file_date}-cdsl-newsletter-{now.strftime('%Y-%m').replace('-', '-')}.md  (csl-guides)
       {now.strftime('%B%Y').lower()}.md                                                (csl-newsletter)
  4. Paste into Buttondown and send.
-->

Dear Sanskrit scholars, students, and dictionary enthusiasts,

<!-- INTRO: 1–2 sentences summarising what this month brought. -->

Here is what happened at the Cologne Digital Sanskrit Dictionaries in {month_year}.

<!-- HIGHLIGHTS: replace the activity log below with 3–5 named sections. -->

<!-- truncate -->

## Activity log ({period})

{activity_block}

---

## Get involved

- **Corrections** — found an error? [Report it](https://sanskrit-lexicon.github.io/csl-guides/contributing/report-a-typo)
- **Archive** — all editions at [/news](https://sanskrit-lexicon.github.io/csl-guides/news) and [csl-newsletter](https://github.com/{ORG}/csl-newsletter)
- **Live site** — [sanskrit-lexicon.uni-koeln.de](https://www.sanskrit-lexicon.uni-koeln.de)

To unsubscribe, use the link at the bottom of this email.
"""

    if args.output == '-':
        print(draft)
    else:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(draft)
        print(f"Draft written to {args.output}", file=sys.stderr)


if __name__ == '__main__':
    main()

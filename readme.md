# csl-newsletter

_Created: 04-10-2021 · Last updated: 06-08-2026_

Archive and tooling home for the email newsletter of the
[Cologne Digital Sanskrit Dictionaries](https://www.sanskrit-lexicon.uni-koeln.de)
(CDSL) project.

Each edition is stored here as a Markdown file — `{month}{year}.md` for a monthly
edition (e.g. [`july2026.md`](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/july2026.md))
and `annual{year}.md` for a year-in-review (e.g.
[`annual2025.md`](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/annual2025.md)) —
holding the plain-text email content in Markdown. The same editions are also
published as blog posts on the guides site at
[/news](https://sanskrit-lexicon.github.io/csl-guides/news).

## Delivery channel — being set up

The delivery mechanism for the 2026 revival is **not yet live**. The intended
tool is [Buttondown](https://buttondown.com), but the account is not yet created
and the channel choice (Buttondown vs a reply-to-list such as Groups.io) is still
an open decision. Until that is resolved, editions live here and on the blog only;
none of the 2026 editions have been mailed to subscribers yet. A subscribe page is
staged at
[csl-guides/users/newsletter](https://sanskrit-lexicon.github.io/csl-guides/users/newsletter).

## Documentation

- [docs/PUBLISH_MANUAL.md](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/docs/PUBLISH_MANUAL.md) — **operator manual**: the full publish workflow (draft with explicit windows → prose edit → edition + archive row → csl-guides blog twin → the pending send step), symptom→cause→cure. The `/cdsl-newsletter-publisher` skill is the automated path; the manual is the human fallback and its specification.

## Tooling

[`scripts/draft-newsletter.py`](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/scripts/draft-newsletter.py)
uses the `gh` CLI to pull commits and closed issues from every active repo in the
`sanskrit-lexicon` org over a date window, then writes a structured Markdown draft
(Docusaurus blog frontmatter + an activity log to be rewritten into prose
highlights). Requires `gh auth login`.

```sh
python scripts/draft-newsletter.py                                  # last 30 days → stdout
python scripts/draft-newsletter.py --since 2026-07-01 --until 2026-07-31 --output draft.md
```

The end-to-end draft → edit → commit → blog → send workflow (and how this repo
pairs with the [csl-guides](https://github.com/sanskrit-lexicon/csl-guides) blog)
is documented in
[`CLAUDE.md`](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/CLAUDE.md)
and encoded in the `/cdsl-newsletter-publisher` workflow skill.

## Archive

### Annual editions

| Year | Link |
| --- | --- |
| 2026 (Jan–Jun) | [2026 year in review](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/annual2026.md) |
| 2025 | [2025 year in review](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/annual2025.md) |
| 2024 | [2024 year in review](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/annual2024.md) |
| 2023 | [2023 year in review](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/annual2023.md) |
| 2022 | [2022 year in review](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/annual2022.md) |
| 2021 | [2021 year in review](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/annual2021.md) |
| 2020 | [2020 year in review](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/annual2020.md) |
| 2019 | [2019 year in review](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/annual2019.md) |
| 2018 | [2018 year in review](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/annual2018.md) |
| 2017 | [2017 year in review](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/annual2017.md) |
| 2016 | [2016 year in review](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/annual2016.md) |
| 2015 | [2015 year in review](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/annual2015.md) |
| 2014 | [2014 year in review](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/annual2014.md) |

### Monthly editions

The 2026 monthly editions revive a series that previously ran in 2021–2023. The
August–December 2026 files are **placeholder templates** (draft skeletons awaiting
content), not finished editions.

| Year | Month | Status | Link |
| --- | --- | --- | --- |
| 2026 | December | template | [December, 2026](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/december2026.md) |
| 2026 | November | template | [November, 2026](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/november2026.md) |
| 2026 | October | template | [October, 2026](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/october2026.md) |
| 2026 | September | template | [September, 2026](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/september2026.md) |
| 2026 | August | drafted | [August, 2026](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/august2026.md) |
| 2026 | July | drafted | [July, 2026](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/july2026.md) |
| 2026 | June | drafted | [June, 2026](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/june2026.md) |
| 2023 | July | archived | [July, 2023](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/july2023.md) |
| 2023 | June | archived | [June, 2023](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/june2023.md) |
| 2023 | April | archived | [April, 2023](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/april2023.md) |
| 2023 | January | archived | [January, 2023](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/january2023.md) |
| 2022 | December | archived | [December, 2022](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/december2022.md) |
| 2022 | November | archived | [November, 2022](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/november2022.md) |
| 2022 | October | archived | [October, 2022](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/october2022.md) |
| 2022 | September | archived | [September, 2022](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/september2022.md) |
| 2022 | August | archived | [August, 2022](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/august2022.md) |
| 2022 | July | archived | [July, 2022](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/july2022.md) |
| 2022 | June | archived | [June, 2022](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/june2022.md) |
| 2022 | May | archived | [May, 2022](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/may2022.md) |
| 2022 | April | archived | [April, 2022](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/april2022.md) |
| 2022 | March | archived | [March, 2022](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/march2022.md) |
| 2022 | February | archived | [February, 2022](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/february2022.md) |
| 2022 | January | archived | [January, 2022](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/january2022.md) |
| 2021 | December | archived | [December, 2021](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/december2021.md) |
| 2021 | November | archived | [November, 2021](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/november2021.md) |
| 2021 | October | archived | [October, 2021](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/october2021.md) |
| 2021 | September | archived | [September, 2021](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/september2021.md) |

## License

Released under [GPL-3.0](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/LICENSE),
consistent with the wider CDSL project.

_Dr. Mārcis Gasūns_
</content>
</invoke>

_Dr. Mārcis Gasūns_

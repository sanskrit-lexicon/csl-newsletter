# PUBLISH_MANUAL.md — metadoc

_Created: 11-07-2026 · Last updated: 11-07-2026_

Companion record for
[docs/PUBLISH_MANUAL.md](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/docs/PUBLISH_MANUAL.md).

## Purpose

The end-to-end publish runbook for a CDSL newsletter edition: draft
generation with explicit windows, the human prose-editing step, the
two-repo pairing (archive file + csl-guides blog post), and the pending
delivery step. Doubles as the specification the
`/cdsl-newsletter-publisher` skill must stay in sync with.

## Audience

- A human publishing a monthly/annual edition without the skill.
- An agent-session author updating the skill (this manual is the spec).
- MG, for the open delivery-channel decision the manual keeps flagged.

## Provenance

Authored 11-07-2026 by Fable 5 (`claude-fable-5`) under handoff
[H514-Fable_csl-newsletter_compile_publish_manual_10.07.26](https://github.com/gasyoun/Uprava/blob/main/handoffs/archive/H514-Fable_csl-newsletter_compile_publish_manual_10.07.26.md)
(the H501–H531 per-repo manuals programme, Litpam-Indexator MANUAL.md gold
standard). Content read from readme.md (H549-refreshed, current truth),
CLAUDE.md (workflow of record, one stale claim), `draft-newsletter.py`,
the june2026 edition, and the `/cdsl-newsletter-publisher` skill — none
invented.

## Ranked improvement backlog

| # | Item | Status |
|---|---|---|
| 1 | Resolve the delivery channel (Buttondown vs Groups.io) — MG `@DECIDE`; then update CLAUDE.md, readme, this manual, and the skill in one pass | open (MG-gated) |
| 2 | Fix CLAUDE.md's "delivery is handled via Buttondown" to "planned" until #1 lands | open |
| 3 | Make `draft-newsletter.py` report per-repo API failures instead of silently returning empty (a partial-auth run currently yields a plausible incomplete draft) | open |
| 4 | A consistency check: every committed edition has its readme row + csl-guides blog twin (the §7 pairing invariant, currently unenforced) | open |
| 5 | Record send dates once delivery goes live (a `Sent:` line or readme column) | open |

## Known limitations

- The prose-editing step is deliberately manual — the manual specifies its
  register and shape but cannot automate judgment.
- csl-guides build mechanics are documented only as an interface
  (`npm run build`); its own docs govern.
- The Buttondown send step is described prospectively — no send has
  happened; revise §3.5 at channel go-live.

## Related documents

- [readme.md](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/readme.md) — archive index + delivery-channel status of record
- [CLAUDE.md](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/CLAUDE.md) — workflow + file-format reference (one stale delivery claim, backlog #2)
- [scripts/draft-newsletter.py](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/scripts/draft-newsletter.py) — the generator
- [june2026.md](https://github.com/sanskrit-lexicon/csl-newsletter/blob/main/june2026.md) — the edition template
- The `/cdsl-newsletter-publisher` workflow skill (claude-config; mirrored to Codex) — the automated path this manual specifies

## Revision history

| Date | Change | By |
|---|---|---|
| 11-07-2026 | Initial version (H514) | Fable 5 (`claude-fable-5`) |

---

_Dr. Mārcis Gasūns_

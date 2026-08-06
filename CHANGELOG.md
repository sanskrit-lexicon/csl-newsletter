# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en.0.3.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2026-08-06

### Added

- August 2026 edition — full prose draft covering July 2026 activity (Benfey
  literary-source overhaul, H1523 security sweep, Salt multidict API, preface
  legend stores, csl-atlas releases, KeySwap, daily corrections); archive row
  flipped template → drafted (H1853)

### Fixed

- `scripts/draft-newsletter.py`: `gh api --paginate` returns one JSON array per
  page, which a single `json.loads` rejects — the harvest silently reported
  "0 of 0 repos active"; now decoded page-by-page and flattened

## [0.1.0] - 2026-06-30

### Added

- Initial release of csl-newsletter
- Monthly newsletter templates for 2026 (August–December)
- Annual editions for years 2014–2026
- July 2026 edition
- Draft script with `--until` flag for preview workflow

### Changed

### Deprecated

### Removed

### Fixed

### Security

[0.2.0]: https://github.com/sanskrit-lexicon/csl-newsletter/releases/tag/v0.2.0
[0.1.0]: https://github.com/sanskrit-lexicon/csl-newsletter/releases/tag/v0.1.0

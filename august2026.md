_Created: 29-06-2026 · Last updated: 05-09-2026_

Date: Mon, 31 Aug 2026
Subject: Cologne Sanskrit Dictionaries update (August 2026)

Dear Sanskrit scholars, students, and dictionary enthusiasts,

Here is the August 2026 edition of the Cologne Digital Sanskrit Dictionaries newsletter,
covering the activity of the past month. Significant work this period: a complete
literary-source overhaul of the Benfey dictionary, a second and much deeper security
hardening pass across the web interfaces, a multi-dictionary endpoint for the new
structured API, and the preface digitisation effort maturing from raw OCR into
machine-readable abbreviation data.


- Benfey dictionary: literary sources linked, sub-headwords promoted

Benfey's Sanskrit-English Dictionary (BEN) received a month-long structural overhaul.
Its literary-source references — previously plain abbreviations in the text — were
normalised to the same consistent markup PWG uses, covering bare references, page
numbers, and dozens of per-work adjustment passes (Śākuntala, Hitopadeśa, Nala,
Kirātārjunīya, and many more). Sub-headwords were then promoted to full headwords, and
homonym numbering was added. Thirteen markup and correction issues were closed in the
BEN repository in July, and the headword normalisation databases (hwnorm1, hwnorm2)
were regenerated to pick up the new headwords. As a result, BEN's literary sources are
now linked in the online display, like PWG and PW before it:

https://github.com/sanskrit-lexicon/BEN/issues


- Security and reliability: the July sweep of the web interfaces

Following June's static-analysis scan, July went considerably deeper. Every display
surface of the two web frontends (csl-websanlexicon and csl-apidev) now escapes
dynamic HTML; standard security headers were added to all server entry points; the
bundled jQuery copies across the display sites (GRA, SKD, MW demo pages, mw-dev, the
verb tables) were brought up to 3.7.1; and the abandoned jquery.cookie plugin was
replaced by js-cookie throughout. The same sweep fixed long-standing user-facing bugs:
scan pages now always offer a direct open-PDF link (helping Firefox on Android, where
embedded PDFs never rendered), the duplicate display of identical MW entries is gone,
Advanced Search highlighting now handles Unicode correctly, and AP90 compound headers
display properly. Twelve issues were closed in csl-websanlexicon and six in csl-apidev
during the month.


- Salt API: one request, many dictionaries

The structured API introduced last month gained a multi-dictionary endpoint: a single
request can now query several dictionaries at once, with parameters for field
selection, result size and ordering, and optional Devanagari output (requested in
csl-orig issue #2881, "single interface for online requests"). On the user-facing
side, the lookup interface shipped its third feature wave: links to the scanned page
images, a copy-citation button, a Vedic-accent toggle, and a dark mode.


- Prefaces: from scanned pages to machine-readable abbreviation data

The front-matter digitisation reported in the previous two editions moved from raw OCR
to structured data. Page-boundary OCR omissions were repaired for the Böhtlingk–Roth
volumes (PWG, PW, PWK), abbreviation keys were aligned to the naming used in the body
texts, and machine-readable "legend stores" — the abbreviation legends of each
dictionary as data — were emitted for PWG and PW, with a schema and parity checks.
The Abbreviations page on the guides site now consumes these legends directly. A new
repository was also created for the front matter of the Deccan College dictionary
(PD), with its own OCR pipeline:

https://sanskrit-lexicon.github.io/csl-guides/


- Measuring the collection: the dictionary atlas

The csl-atlas repository, which studies the dictionary collection quantitatively,
shipped fourteen releases in July. New analyses include a per-dictionary
"entry anatomy" radar chart, a data-richness typology grading every dictionary from
L0 to L10, a census of orthographic drift in the glosses, and a measured study of
completion horizons — how long large dictionaries actually take to finish — comparing
the in-progress Deccan College dictionary with AP, PWG and MW. All datasets and
visualisations are committed and reproducible in the repository:

https://github.com/sanskrit-lexicon/csl-atlas


- KeySwap: a typing helper for IAST

The sanskrit-util repository grew a new tool: KeySwap, a cross-platform typing helper
for entering IAST transliteration (Windows via AutoHotkey, with iPhone and Mac
recipes). Type a plain letter and cycle it through its diacritic variants; smart
digraph handling, an optional live headword check against the Cologne server, an
offline SLP1 wordlist fallback, and an opt-in frequency-ranked mode based on the
Digital Corpus of Sanskrit are included. Nine releases (0.8.0 through 0.8.11) landed
in July. The library also fixed its iast_to_devanagari function, which previously
produced broken output for consonant+vowel sequences.

https://github.com/sanskrit-lexicon/sanskrit-util


- Text corrections: the daily cadence continues

The daily correction workflow ran through the month: the daily batches through
10 July were filed and closed (seventeen daily-correction issues), a consolidated
AP90 batch was promoted into the source repository, and the offline StarDict
dictionaries were regenerated automatically after every correction commit. In the
central COLOGNE tracker, twenty-one long-standing discussion issues were reviewed and
closed.

To report an error or suggest a correction:
https://github.com/sanskrit-lexicon/CORRECTIONS/issues/new


Corrections and feedback are always welcome:
https://github.com/sanskrit-lexicon/csl-guides/issues

------------------------------------------------------------
Useful links:

Cologne Digital Sanskrit Dictionaries
https://www.sanskrit-lexicon.uni-koeln.de

Documentation and guides
https://sanskrit-lexicon.github.io/csl-guides/

Newsletter archive (GitHub)
https://github.com/sanskrit-lexicon/csl-newsletter

Newsletter archive (web)
https://sanskrit-lexicon.github.io/csl-guides/news

Subscribe to future editions
https://sanskrit-lexicon.github.io/csl-guides/users/newsletter

To unsubscribe from future updates, reply with "unsubscribe" in the subject line.

_Dr. Mārcis Gasūns_

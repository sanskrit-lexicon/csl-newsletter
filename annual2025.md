Date: Wed, 31 Dec 2025
Subject: Cologne Sanskrit Dictionaries year in review (2025)

Dear Sanskrit scholars, students, and dictionary enthusiasts,

2025 was a year of expanded reach: the Frisch Sanskrit Reader was added as a new
dictionary, the PWG link-splitting programme resolved dozens of compound literary-source
references, a large-scale XML transformation was undertaken in the COLOGNE repository, and
search transliteration handling was improved for the first time in several years.


- Frisch Sanskrit Reader added to CDSL

The Frisch Sanskrit Reader (originally Oldřich Fryš, Санскритская хрестоматия, Moscow:
ABV 2015, vol. 2) was integrated into the csl-pywork pipeline and given an initial CDSL
version in 2025. This bilingual Sanskrit–Russian text had not previously been available in
the standard CDSL infrastructure. The data lives in the FRI repository and extends the
corpus beyond the classical dictionary genre.


- PWG link-splitting: 30+ compound source references resolved

The ongoing work of making abbreviated literary-source references in the Böhtlingk-Roth
dictionaries (PWG and PW) clickable reached a major milestone in 2025. Issue #160 in the
PWG repository tracked the splitting of compound references — cases where a single `<ls>`
tag covers multiple pages or editions. In 2025, more than thirty compound-reference
patterns were resolved, including RAGH. (Raghuvaṃśa), ŚAT. BR. (Śatapathabrāhmaṇa),
YĀJÑ. (Yājñavalkya), KĀTY. ŚR. (Kātyāyana Śrautasūtra), and PAÑCAT. (Pañcatantra)
in multiple edition variants. The Nirukta link target was also added across PWG, PW,
PWKVN, SCH, and MW.


- COLOGNE: large-scale XML transformation

The COLOGNE repository undertook a systematic XSL-based transformation of markup across
the corpus (#441). A series of XSL stylesheets (labeled aaa through aah) were developed
to normalize tag structures across dictionary files. The work also addressed expanding
the `<ls>` abbreviations into full bibliography entries in a more automated way, using
updated book-name lists.


- Search with transliteration variants

A significant usability improvement landed in the COLOGNE search interface in 2025: the
headword search now accepts multiple transliteration inputs and normalises them before
matching (#443). Literary-source references were made visually distinct (displayed in blue
rather than grey) to improve readability. These changes affect all dictionaries accessible
through the Cologne web interface.


- Scott backlog corrections installed

A substantial backlog of corrections contributed by Scott Ryden was installed in 2025,
covering SHS (Shabda-Sagara) end-of-line hyphenation joining and AP (Apte 1957) entries.
These were processed through the csl-corrections and csl-pywork pipelines and deployed to
the production server.

Corrections and feedback are always welcome through the GitHub repository:
https://github.com/sanskrit-lexicon

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

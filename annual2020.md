Date: Thu, 31 Dec 2020
Subject: Cologne Sanskrit Dictionaries year in review (2020)

Dear Sanskrit scholars, students, and dictionary enthusiasts,

2020 was a productive year for the Cologne Digital Sanskrit Dictionaries: English
text corrections were completed across many dictionaries, the Python toolchain advanced
toward full Python 3 compatibility, and GRA verb data received significant attention.


- English corrections completed across dictionaries

A major effort to correct English word errors across all dictionaries was under way in
2020 and reached completion this year. The csl-orig repository shows correction batches
applied to AP90 (Apte 1890) and CAE (Cappeller), among others — systematic proofing
passes that improved the accuracy of the English definitions and abbreviation
expansions throughout the corpus.


- Python 3 migration and SQLite improvements

The Python generation pipeline (csl-pywork) received important work in 2020: the
SQLite interface was refactored to use a pure Python implementation rather than relying
on an external sqlite3 executable, improving portability across systems. Alongside this,
the codebase continued its migration from Python 2 to Python 3, necessary as Python 2
reached end-of-life in January 2020.


- Grassmann verb data work

The GRA (Grassmann Wörterbuch zum Rig-Veda) repository received new verb data
contributed by Dmitri, expanding the structured verb form information available for
the Grassmann dictionary. This was part of a longer effort to bring GRA's rich
grammatical data into the same structured format used for other dictionaries.


- PDF display improvements

The web display layer was updated to improve how scan images are served: a local
installation now uses local scan images if available, falling back to the Cologne
server otherwise. This made local development and testing significantly more practical.

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

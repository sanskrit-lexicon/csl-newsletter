Date: Fri, 31 Dec 2021
Subject: Cologne Sanskrit Dictionaries year in review (2021)

Dear Sanskrit scholars, students, and dictionary enthusiasts,

2021 was one of the most active years in the project's GitHub history: the Devanāgarī
display layer launched, Boehtlingk's Indische Sprüche entered preparation, several
dictionaries received extensive markup improvements, and the correction workflow was
formalized with new tooling for users and contributors.


- csl-devanagari: Devanāgarī display launched

A major new feature arrived in September 2021 with the creation of the csl-devanagari
repository, in response to a request by Nagabhushana Rao for dictionary data closer to
the printed text. Two scripts — to_devanagari.py and to_slp1.py — handle round-trip
conversion between SLP1 and Devanāgarī. More than thirty issues were filed and resolved
in the first week alone, addressing edge cases in accented IAST and homophone characters
(ऌ, ळ). The homepage was updated to reflect 38 dictionaries.


- Indische Sprüche preparation begins

The long-anticipated digital edition of Boehtlingk's Indische Sprüche (BOESP) — a
collection of Sanskrit proverbs and quotations — entered active preparation. Jim
Funderburk coordinated a proofreading effort involving Sampada, Andhrabharati, and
Thomas, working through the three-volume ANSI source files. Greek text and link
targets for the BOESP were added to PW and PWG, and the Mahābhārata Calcutta edition
scans were added to provide link targets for the dense citation network.


- INM (Indian Epigraphical Glossary): deep markup improvements

The INM dictionary received sustained attention throughout December: the source file
was split into sub-parts for maintainability, Greek text was added, punctuation in
italic and bold ranges was corrected, and "widely spaced text" markup was introduced.
All line-marker formatting (`<>`, div) was removed across all dictionaries in a
clean-up pass that affected more than a dozen repositories.


- User correction infrastructure expands

The csl-lnum repository was created to give users a way to link directly to specific
line numbers in csl-orig and submit corrections. The cologne-stardict files began
including links to scan pages and correction forms, so stardict users can verify
against the printed text and report errors without navigating the web interface.
User corrections from June through December 2021 were installed in csl-orig.


- GRA and BEN markup advances

Grassmann's Wörterbuch zum Rig-Veda (GRA) gained structured `<ab>` and `<ls>`
abbreviation markup, with support for Grassmann's Verbesserungen und Nachtrage
(corrections and additions). Benfey (BEN) received a new, more legible scan set
and 180 systematic corrections to headword encoding and `<ab>` tags.

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

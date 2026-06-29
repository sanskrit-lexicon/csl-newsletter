Date: Tue, 31 Dec 2024
Subject: Cologne Sanskrit Dictionaries year in review (2024)

Dear Sanskrit scholars, students, and dictionary enthusiasts,

2024 was a year of deep structural work: a major XML conversion brought the internal
format of ten dictionaries into the modern Lbody standard, Monier-Williams received
extensive page-link and display improvements, and the Böhtlingk-Roth (PWG) link-target
programme continued with new literary sources.


- hwextra → Lbody conversion across ten dictionaries

The single largest structural change of the year was the systematic conversion of the
hwextra-Lbody format across the entire CDSL corpus. In 2024 this was completed for:
Vācaspatyam (VCP), Śabdakalpadruma (SKD), Shabda-Sagara (SHS), Böhtlingk kürzere
Fassung with verbal nouns (PWKVN), Böhtlingk-Roth (PW), L.R. Vaidya (LRV), Cappeller
(CAE), Burnouf (BUR), Apte 1890 (AP90), and the Abbreviation Collector (ACC). The
conversion aligns each dictionary's headword and extra-headword material with the
standard pipeline, enabling more consistent cross-dictionary processing going forward.
This was coordinated through a series of dedicated issues (#422–#432) in the COLOGNE
repository and corresponding changes in csl-pywork.


- Monier-Williams: page links, column links, and display fixes

The MW display received sustained attention in 2024. Clickable page and column references
(the `<col>X</col>` tags) were wired up to link directly to the scanned PDF pages of the
1899 print edition (#64). The list display was corrected to suppress artificial homonyms
and to handle special characters (circle-R, circle-S) that had previously disrupted
rendering (#91). The abbreviation file (mwab_input.txt) was revised in several passes
and a large batch of user-submitted corrections was installed. Research into the
authority-source abbreviation list produced expanded tooltip entries for dozens of sources.


- PWG/PW link targets expanded

Work on making the literary-source references in Böhtlingk-Roth (PWG) and the short
version (PW) clickable continued throughout 2024. New link targets were added for Hariv.
(Harivaṃśa), Bhāg. P. (Bhāgavata Purāṇa), and the Manu (Mānavadharmaśāstra) entries
in PWG, PW, PWKVN, SCH, and MW simultaneously. The VN (verbal nouns) section of PWG —
previously incomplete — had its scan pages added and was cross-linked.


- Abbreviation and authority files revised

The csl-pywork repository received multiple rounds of revision to abbreviation and
authority files: mwab_input.txt (MW abbreviations), pwgbib_input.txt (PWG bibliography),
schauth/tooltip.txt (SCH authority), and burab_input.txt (BUR authority). These files
drive the tooltip expansions visible when hovering over abbreviated source references in
the web interface. The SCH abbreviation for Dhātupāṭha (Böhtlingk edition) was corrected
and the MW entry for Bollensen's Mālavikāgnimitra edition was added.

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

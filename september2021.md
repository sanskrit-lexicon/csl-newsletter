# Datewise log

## 01 September 2021

1. csl-orig. https://github.com/sanskrit-lexicon/csl-orig/issues/586
2. csl-corrections. https://github.com/sanskrit-lexicon/csl-corrections/issues/80
3. csl-orig. BHS - add metric symbols. See https://github.com/sanskrit-lexicon/csl-orig/commit/4fb1c8ef88a36cc20657d07302a25714959b5299
4. csl-doc. Documentation updated to guide for pull request .
5. csl-corrections. BHS. print changes made. See https://github.com/sanskrit-lexicon/csl-corrections/commit/0c7cb1aef7d156a6ddf70b4c679607c33d1390d1 and https://github.com/sanskrit-lexicon/csl-corrections/issues/80.
6. funderburkjim/boesp-prep. Preparation of Boehtlingk, Indische Sprüche. See issues https://github.com/funderburkjim/boesp-prep/issues/3, https://github.com/funderburkjim/boesp-prep/issues/4 for details.

## 02 September 2021

1. CORRECTIONS. In the issue https://github.com/sanskrit-lexicon/CORRECTIONS/issues/414#issuecomment-911742190, Mr. Nagabhushana Rao specifically asked for Cologne data in a manner which is nearer to the printed text, rather than having Devanagari data in SLP1 scheme.
2. csl-orig. The issue was further elaborated in https://github.com/sanskrit-lexicon/csl-orig/issues/604 .
3. csl-devanagari. Based on this requirement, development was done and a new repository csl-devanagari was created to cater to this requirement.
4. csl-devanagari. Two scripts `to_devanagari.py` and `to_slp1.py` were written for allowing to and fro conversion to Devanagari and SLP1.
5. csl-devanagari. `to_devanagari.py` script converted a given dictionary to Devanagari and stored in csl-devanagari/v02/dictcode/dictcode.txt.
6. csl-devanagari. `to_devanagari.py` script converted csl-devanagari/v02/dictcode/dictcode.txt to SLP1 and stored in csl-devanagari/slp1/dictcode.txt. Folder slp1 is not tracked via git, because it is supposed to be the same as csl-orig/v02/dictcode/dictcode.txt file.
7. csl-devanagari. A `redo.sh` script was written which ran both `to_devanagri.py` and `to_slp1.py` script on a given dictionary and stored the differences in csl-devanagari/diff/dictcode.txt.

## 03 September 2021

1. csl-devanagari. The differences which were found out in csl-devanagari/diff folder for every dictionary were examined, and necessary corrections were made in either the code or the data to weed out such differences.
2. csl-devanagari. A script `redo_all.sh` was created. See https://github.com/sanskrit-lexicon/csl-devanagari/commit/a09d0236a0e7973b899720d73ddab02d62c2e144#diff-8c5967fd8486f34493710cc39b240aad46536cf4ee421ffd0479e6542db03e36 .
3. csl-devanagari. Issues https://github.com/sanskrit-lexicon/csl-devanagari/issues/1 to https://github.com/sanskrit-lexicon/csl-devanagari/issues/30 were raised. Necessary changes were made. Majority of them were regarding wrong conversion from accented IAST to Devanagari. As Mr. Nagabhushana Rao did not want such a conversion, and was happy with IAST data as it is, majority of issues were resolved. See https://github.com/sanskrit-lexicon/csl-devanagari/issues/4#issuecomment-912456604 for details.
4. csl-devanagari. Some changes were required when there were trailing whitespaces in the meta-line of a few dictionaries. See https://github.com/sanskrit-lexicon/csl-devanagari/issues/9 for example.
5. csl-devanagari. Removed trailing spaces from meta-lines. See https://github.com/sanskrit-lexicon/csl-devanagari/issues/6, https://github.com/sanskrit-lexicon/csl-devanagari/issues/8, https://github.com/sanskrit-lexicon/csl-devanagari/issues/9, https://github.com/sanskrit-lexicon/csl-devanagari/issues/10
6. csl-homepage. Changed display to show 38 dictionaries instead of 37 and the last date to 1993 instead of 1976.
7. funderburkjim/boesp-prep. Changes to boesp-1_ansi, part 3. https://github.com/funderburkjim/boesp-prep/issues/5.

## 04 September 2021

## 05 September 2021

1. funderburkjim/boesp-prep-sam. Sampada starts proofreading of BOESP.
2. funderburkjim/boesp-prep-ab. Andhrabharati starts proofreading of BOESP.

## 06 September 2021

1. csl-orig. Added the missing data as suggested by ?? marks in various dictionaries. See https://github.com/sanskrit-lexicon/CORRECTIONS/issues/92#issuecomment-913174476
2. csl-orig. PW. Removed superfluous `{##}` markup. See https://github.com/sanskrit-lexicon/csl-devanagari/issues/16.
3. csl-orig. PWG. Removed superfluous `{##}` markup. See https://github.com/sanskrit-lexicon/csl-devanagari/issues/17.

## 07 September 2021

1. csl-devanagari. Wrote a script `carry_changes_to_cslorig.sh` to carry changes made in csl-devanagari/v02/dictcode/dictcode.txt file to csl-orig/v02/dictcode/dictcode.txt file.
2. csl-orig. INM. changed Varuna to Varuṇa. See https://github.com/sanskrit-lexicon/csl-orig/issues/612.

## 08 September 2021

1. csl-json. Mr. Neelesh Bodas of https://ashtadhyayi.com/ confirmed that the website uses data directly from csl-json repository. It is realtime. Thus, the downstream users who use https://ashtadhyayi.com/ for searching Sanskrit dictionaries get benefits of latest data from Cologne. See https://github.com/sanskrit-lexicon/csl-json/issues/5#issuecomment-914911576 for details.
2. csl-orig. GST. Add lang tag. See https://github.com/sanskrit-lexicon/csl-orig/issues/610.

## 09 September 2021

1. csl-orig. BEN. ab and ls markup preparation made.
2. csl-pywork. `xmlchk_xampp.sh` added in v02 to check validity of XML.

## 10 September 2021

1. csl-orig. BEN. ab and ls markup made. See https://github.com/sanskrit-lexicon/BEN/issues/2 for details.
2. csl-pywork. BEN. ab and ls markup support added for code. See https://github.com/sanskrit-lexicon/csl-pywork/commit/ac963e356bb1eb248dd4810ebb6ee8cf1588a39a .
3. csl-websanlexicon. Added BEN to dictionaries with ls markup.

## 11 September 2021

1. csl-pywork. GRA. go.=gothic abbreviation support added.

## 12 September 2021

1. cologne-stardict. Removed dependency of `make_babylon.py` script on `lxml` module. lxml is difficult to install on windows, and is an overkill in the context. The script was modified to use native python xml.etree module.
2. csl-orig. GRA. Added `<ab>` markup for Fi., Ku., BR., Be. SV. gl., Be. SV. gloss., Be. See https://github.com/sanskrit-lexicon/csl-orig/issues/616 and https://github.com/sanskrit-lexicon/GRA/issues/18 for details.
3. csl-pywork. GRA. Abbreviations added. See https://github.com/sanskrit-lexicon/csl-pywork/commit/04b181da7f39c1daa21c2bc5d886a66900eb173c .
4. csl-pywork. `sqlite.py` and `xmlvalidate.py` now use python3 instead of python2, thus reducing dependence on python2. See https://github.com/sanskrit-lexicon/csl-pywork/issues/28.

## 13 September 2021

1. csl-devanagari. An error crept into indic-transliteration package which converted `1/6` in slp1 encoding to `१꣡६` in Devanagari encoding. Raised the issue at https://github.com/indic-transliteration/indic_transliteration_py/issues/68 . This bug has resulted in alteration in many dictionaries. Keeping them on hold till the correction happens.
2. sanskrit-lexicon-scans. KRM. Scan page is cut at one location. Jim suggested that someone can look at all the scan pages and decide the pages which are sub par. See https://github.com/sanskrit-lexicon-scans/krm/issues/1#issuecomment-917718003
3. csl-pywork. Readme for `redo_xampp_selective.sh` script added. See https://github.com/sanskrit-lexicon/csl-pywork/blob/master/v02/readme_selective.md . This script is to be used only for cronjob to update csl-json and cologne-stardict and indic-dict/stardict-sanskrit repository based on changes in csl-orig repository on reboot of Dhaval's computer.
4. csl-homepage. `update_version.sh` script added. See https://github.com/sanskrit-lexicon/csl-homepage/issues/9 for details.
5. COLOGNE. xmltags in csl-orig have been analysed. See https://github.com/sanskrit-lexicon/COLOGNE/issues/366.

## 14 September 2021

1. csl-homepage. Homepage now shows version number at two places i.e. in header and in bibliographic reference. See https://github.com/sanskrit-lexicon/csl-homepage/issues/9. Also see https://github.com/sanskrit-lexicon/csl-orig/issues/6#issuecomment-907084632.
2. csl-homepage. AP90, AE. Dictionary year of publication was goofed up earlier. Correction made. See https://github.com/sanskrit-lexicon/csl-homepage/issues/6.
3. csl-homepage. CLARIN tooltip correction made. See https://github.com/sanskrit-lexicon/csl-homepage/issues/10.
4. csl-orig. GST. Advertisement of the books of author is moved out of csl-orig/v02/gst/gst.txt file and put at csl-orig/v02/gst/gst_advertisement.txt file. See https://github.com/sanskrit-lexicon/csl-orig/issues/611 for details.
5. sanskrit-lexicon/BOR - new repository BOR started. It is being used to track development of various improvements specific to BOR dictionary.

## 15 September 2021

1. GreekInSanskrit. BOESP. Greek text for BOESP has been provided. https://github.com/sanskrit-lexicon/GreekInSanskrit/issues/33 and https://github.com/sanskrit-lexicon/GreekInSanskrit/issues/42.
2. GreekInSanskrit. BHS, GST, VEI. Greek texts for BHS, GST and VEI have been provided. See issues https://github.com/sanskrit-lexicon/GreekInSanskrit/issues/37, https://github.com/sanskrit-lexicon/GreekInSanskrit/issues/38 and https://github.com/sanskrit-lexicon/GreekInSanskrit/issues/40.
3. csl-orig. BUR. Corrected Devanagari IAST differences in BUR dictionary. See https://github.com/sanskrit-lexicon/csl-orig/issues/626.
4. csl-orig. BOR. Broken bar inside Sanskrit text converted to danda. See https://github.com/sanskrit-lexicon/csl-orig/issues/625. 

## 16 September 2021

## 17 September 2021

1. GreekInSanskrit. BOESP. Greek notes and addenda in BOESP added by Jonathan Migliori. See https://github.com/sanskrit-lexicon/GreekInSanskrit/issues/42.
2. csl-corrections. Documentation on how to update cfr.tsv file to process corrections submitted by users via Cologne website is described by Jim Funderburk. See https://github.com/sanskrit-lexicon/csl-corrections/issues/81.

## 18 September 2021

1. alternateheadwords. Added pending alternate headwords in AP90. See https://github.com/sanskrit-lexicon/alternateheadwords/issues/7#issuecomment-921890375.
2. csl-devanagari. Nagabhushana Rao does proofreading of headwords of IEG dictionay. See https://github.com/sanskrit-lexicon/csl-devanagari/issues/31.
3. csl-orig. BUR. Correct the cases where Devangari and IAST headowrds differ. See https://github.com/sanskrit-lexicon/csl-orig/issues/626.
4. csl-orig. BEN, MD, MW72, PD. Comparision of Devanagari and IAST headwords started. See https://github.com/sanskrit-lexicon/csl-orig/issues/627, https://github.com/sanskrit-lexicon/csl-orig/issues/628, https://github.com/sanskrit-lexicon/csl-orig/issues/629, https://github.com/sanskrit-lexicon/csl-orig/issues/630.

## 19 September 2021

1. csl-corrections. A very long standing issue of correction of English words from dictionary entries came to a conclusion today. The process lasted for almost a year. See https://github.com/sanskrit-lexicon/csl-corrections/issues/14#issuecomment-890351243.

## 20 September 2021

1. funderburkjim/boesp-prep. Greek translations for BOESP provided. See https://github.com/funderburkjim/boesp-prep/issues/16.

## 21 September 2021

## 22 September 2021

## 23 September 2021

1. csl-orig. SCH. Homonym number appears before IAST headword .
2. csl-orig. SCH. º is changed to °.
3. csl-orig. PWG. prefix data issues corrected. See https://github.com/sanskrit-lexicon/csl-orig/issues/632.
4. csl-orig. SCH. + changed to daggar. See https://github.com/sanskrit-lexicon/PWK/issues/74#issuecomment-925961439.
5. csl-orig. SCH. ^X changed to <sup>X</sup>.
6. csl-pywork. SCH. `make_xml.py` modified for displaying SCH headword properly. See https://github.com/sanskrit-lexicon/csl-pywork/commit/b3bc04a3c04a394785f21d5917e79a349225e774.
7. csl-pywork. Recent change in sch-meta2.txt file created a problem of infinite loop in `redo_xampp_selective.sh` file. Necessary change is made in script to ignore such files in processing. See https://github.com/sanskrit-lexicon/csl-pywork/commit/6ec917e736cf6209c380dcb1ec719a1cc2d34921.
7. csl-websanlexicon. SCH. display code tweak removed, because <sup> tag is now present in sch.txt itself.
8. PWK. Various steps attempted for VN and SCH comparision.

## 24 September 2021

1. COLOGNE. Extended ASCII analysis done. See https://github.com/sanskrit-lexicon/COLOGNE/issues/368.
2. COLOGNE. Changed masculine ordinal indicator to degree sign. See https://github.com/sanskrit-lexicon/COLOGNE/issues/369.

## 25 September 2021

1. csl-orig. ACC, AP90, BEN, GST, IEG, INM, KRM, MCI, MW72, PWG, SHS, VEI, YAT. Total of 13 dictionaries had º changed to °. See https://github.com/sanskrit-lexicon/csl-orig/commit/a4dbbe367f4458452d554fb6ad9c0cc3ca2b11c6 .
2. csl-pywork. As Jim was not inclined to try cronjob for Cologne server, removed the file `redo_cologne_selective.sh` from repository.

## 26 September 2021

1. PWK. PWK3 VN pages 256-265 digitized. See https://github.com/sanskrit-lexicon/PWK/issues/76.

## 27 September 2021

1. cologne-stardict. Earlier the babylon files were generated from XML files. Now the code is refactored to generate babylon files from text file directly. The work continued for next 3-4 days.

## 28 September 2021

1. csl-orig. SCH. °+ changed to †°.
2. cologne-stardict. Alternate headwords from xxx_hwextra.txt file is also integrated in babylon file, and hence in stardict file too. See https://github.com/sanskrit-lexicon/cologne-stardict/issues/21.
3. csl-orig. A few cases of `ab` tag inside the `{%....%}` tag was noted in BEN. See https://github.com/sanskrit-lexicon/csl-orig/issues/633.

## 29 September 2021

## 30 September 2021

1. csl-orig. SCH. Corrections noticed during comparision with PWK-nachtrage volume 3 were incorporated. See https://github.com/sanskrit-lexicon/csl-orig/commit/21a719c38e800bf98a9177f69940436e85e891e3 and sanskrit-lexicon/PWK#77 for details.

# Brewing ideas

1. Make line markers uniform across dictionaries. See https://github.com/sanskrit-lexicon/csl-devanagari/issues/26 . 
2. SCH has many double spaces. Need to convert to single space. See https://github.com/sanskrit-lexicon/csl-devanagari/issues/27#issuecomment-913587330.
3. Do jihvAmUlIya and upadhmAnIya require different encoding? See https://github.com/sanskrit-lexicon/csl-devanagari/issues/29 .
4. Add ab,ls tags for GRA (and may be other dictionaries too). See https://github.com/sanskrit-lexicon/GRA/issues/18 .
5. Remove non-Devanagari markup outside scope of `{##}` tags. See https://github.com/sanskrit-lexicon/csl-devanagari/issues/10
6. A cronjob for Cologne jobs. Jim is not yet convinced about the utility or safety of this approach. See https://github.com/sanskrit-lexicon/csl-homepage/commit/830689231db8e12164cdf8cf9f82fbdf16e43d50.
7. PDF download to be made more accessible. See https://github.com/sanskrit-lexicon/COLOGNE/issues/367
8. Check the scans to find out pages having blurred images / cut images.
9. How to handle non-Sanskrit headwords in dictionaries such as IEG? See https://github.com/sanskrit-lexicon/csl-corrections/issues/69
10. There may be some cases of difference between key1 and key2. They need to be examined further. See https://github.com/sanskrit-lexicon/csl-orig/issues/621#issuecomment-922125549
11. Identify proper names across dictionaries. See https://github.com/sanskrit-lexicon/MWS/issues/24.
12. Grasmann missing annexure pages need to be digitized. See https://github.com/sanskrit-lexicon/GRA/issues/17.
13. Give facility of corrections to stardict users for a given entry. See https://github.com/indic-dict/stardict-sanskrit/issues/122.
14. Handle non-Sanskrit headwords in a better way. See https://github.com/sanskrit-lexicon/csl-corrections/issues/69.
15. Handle proper names better in SLP1 transliteration. https://github.com/sanskrit-lexicon/MWS/issues/24#issuecomment-922161963.
16. GRA. Digitize VN and Nachtrage pages. See https://github.com/sanskrit-lexicon/GRA/issues/17.
17. cologne-stardict. Add correction links to stardict files of Cologne, so that a user can directly submit correction to the respective entry itself, without going through bulky files of csl-orig repository. See https://github.com/indic-dict/stardict-sanskrit/issues/122.
18. COLOGNE. handle jihvāmūlīya and upadhmānīya properly. See https://github.com/sanskrit-lexicon/COLOGNE/issues/59#issuecomment-899037966.
19. SCH. Partial translation of preface of SCH. See https://github.com/sanskrit-lexicon/SCH/issues/6.
20. PWK. Comparision between PWK-VN and SCH thought of. https://github.com/sanskrit-lexicon/PWK/issues/70.
21. csl-pywork. Create `make_html.py` file in addition to `make_xml.py`. This can pregenerate HTML data for display. See https://github.com/sanskrit-lexicon/COLOGNE/issues/291#issuecomment-922401908.
22. csl-orig. Use some consisten way to denote ऌ and ळ in IAST, while preserving invertibility. See https://github.com/sanskrit-lexicon/csl-orig/issues/631.
23. COLOGNE. Track missing scans and missing digitizations across dictionaries. See https://github.com/sanskrit-lexicon/COLOGNE/issues/363.
24. csl-orig. Remove line breaks from xxx.txt files. See https://github.com/sanskrit-lexicon/csl-devanagari/issues/26#issuecomment-924512081.
25. PWG. Various additions to PWG were discussed. They may be handled as and when situation is conducive. See https://github.com/sanskrit-lexicon/PWG/issues/37.
26. COLOGNE. Check for missing links. Earlier, some approach using `xenu` tool was being explored. See https://github.com/sanskrit-lexicon/COLOGNE/issues/370.
27. MCI. Add printed book categories in display. See https://github.com/sanskrit-lexicon/MCI/issues/1#issuecomment-927264425.
28. cologne-stardict. Make babylon file directly from csl-orig/v02/xxx/xxx.txt file, instead of xxx.xml file. See https://github.com/sanskrit-lexicon/cologne-stardict/issues/20.

# Execution status

1. csl-json - This repository was started to create JSON files for use of https://ashtadhyayi.com/kosha/ on 16 August 2021.
2. csl-json - A redo.sh script was added to regenerate JSON files of all dictionaries on 16 August 2021.
3. csl-json - script `json_from_babylon.py` was commented for easier comprehension on 16 August 2021.
4. csl-json - This repository is getting regular updates as and when some data in csl-orig is changed and Dhaval's computer is rebooted from 16 August 2021 onwards.
5. csl-json - Mr. Neelesh Bodas of https://ashtadhyayi.com/ confirmed that the website uses data directly from csl-json repository. It is realtime. Thus, the downstream users who use https://ashtadhyayi.com/ for searching Sanskrit dictionaries get benefits of latest data from Cologne. See https://github.com/sanskrit-lexicon/csl-json/issues/5#issuecomment-914911576 for details. Discussion was on 08 September 2021.
6. cologne-stardict - `make_babylon.py` script was updated to use new location of licence file. See https://github.com/sanskrit-lexicon/cologne-stardict/commit/07463d426454dcf933373b7fbd359dc2c03e8a2b on 16 August 2021.
7. cologne-stardict - `redo.sh` script was extended to new dictionary Abhidhānaratnamālā of Halāyudha (ARMH) on 16 August 2021.
8. cologne-stardict - `move_to_stardict.sh` script was updated to accomodate the change in the directory indic-dict/stardict-sanskrit. In the current arrangements, indic-dict directory is sibling of cologne directory. See https://github.com/sanskrit-lexicon/cologne-stardict/commit/07463d426454dcf933373b7fbd359dc2c03e8a2b. 16 August 2021.
9. cologne-stardict - Earlier, production directory of this repository was not tracked. Now, it is also tracked.
10. cologne-stardict - Removed dependency of `make_babylon.py` script on `lxml` module. lxml is difficult to install on windows, and is an overkill in the context. The script was modified to use native python xml.etree module. 12 September 2021.
11. Compare the IAST and Devanagari headwords in the dictionaries BEN, BUR, MD, MW72, MW and PD. See https://github.com/sanskrit-lexicon/COLOGNE/issues/180 for details.
12. Corrections of English errors was completed in all dictionaries. See https://github.com/sanskrit-lexicon/csl-corrections/issues/14#issuecomment-890351243 for details.

# Data correction

1. https://github.com/sanskrit-lexicon/csl-orig/issues/586
2. https://github.com/sanskrit-lexicon/csl-corrections/issues/80
3. BHS - add metric symbols. See https://github.com/sanskrit-lexicon/csl-orig/commit/4fb1c8ef88a36cc20657d07302a25714959b5299

# Programmatic development


# Todo list


# Repositories to be covered in newsletter

1. csl-orig
2. csl-pywork
3. csl-websanlexicon
4. csl-homepage
5. csl-doc
6. csl-json
7. csl-devanagari
8. cologne-stardict
9. csl-lnum
10. sanskrit-lexicon-scans
11. csl-corrections
12. CORRECTIONS
13. COLOGNE
14. Dictionarywise repositories for the following dicts. 
`acc ae ap ap90 ben bhs bop bor bur cae ccs gra gst ieg inm krm mci md mw mw72 mwe pd pe pgn pui pw pwg sch shs skd snp stc vcp vei wil yat lan armh`
15. funderburkjim/boesp-prep
16. funderburkjim/boesp-prep-sam
17. funderburkjim/boesp-prep-ab


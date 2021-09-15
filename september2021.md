# Datewise log

## 01 September 2021

1. https://github.com/sanskrit-lexicon/csl-orig/issues/586
2. https://github.com/sanskrit-lexicon/csl-corrections/issues/80
3. BHS - add metric symbols. See https://github.com/sanskrit-lexicon/csl-orig/commit/4fb1c8ef88a36cc20657d07302a25714959b5299

## 02 September 2021

1. In the issue https://github.com/sanskrit-lexicon/CORRECTIONS/issues/414#issuecomment-911742190, Mr. Nagabhushana Rao specifically asked for Cologne data in a manner which is nearer to the printed text, rather than having Devanagari data in SLP1 scheme.
2. The issue was further elaborated in https://github.com/sanskrit-lexicon/csl-orig/issues/604 .
3. Based on this requirement, development was done and a new repository csl-devanagari was created to cater to this requirement.
4. Two scripts `to_devanagari.py` and `to_slp1.py` were written for allowing to and fro conversion to Devanagari and SLP1.
5. `to_devanagari.py` script converted a given dictionary to Devanagari and stored in csl-devanagari/v02/dictcode/dictcode.txt.
6. `to_devanagari.py` script converted csl-devanagari/v02/dictcode/dictcode.txt to SLP1 and stored in csl-devanagari/slp1/dictcode.txt. Folder slp1 is not tracked via git, because it is supposed to be the same as csl-orig/v02/dictcode/dictcode.txt file.
7. A `redo.sh` script was written which ran both `to_devanagri.py` and `to_slp1.py` script on a given dictionary and stored the differences in csl-devanagari/diff/dictcode.txt.

## 03 September 2021

1. The differences which were found out in csl-devanagari/diff folder for every dictionary were examined, and necessary corrections were made in either the code or the data to weed out such differences.
2. A script `redo_all.sh` was created. See https://github.com/sanskrit-lexicon/csl-devanagari/commit/a09d0236a0e7973b899720d73ddab02d62c2e144#diff-8c5967fd8486f34493710cc39b240aad46536cf4ee421ffd0479e6542db03e36 .
3. Issues https://github.com/sanskrit-lexicon/csl-devanagari/issues/1 to https://github.com/sanskrit-lexicon/csl-devanagari/issues/30 were raised. Necessary changes were made. Majority of them were regarding wrong conversion from accented IAST to Devanagari. As Mr. Nagabhushana Rao did not want such a conversion, and was happy with IAST data as it is, majority of issues were resolved. See https://github.com/sanskrit-lexicon/csl-devanagari/issues/4#issuecomment-912456604 for details.
4. Some changes were required when there were trailing whitespaces in the meta-line of a few dictionaries. See https://github.com/sanskrit-lexicon/csl-devanagari/issues/9 for example.
5. Removed trailing spaces from meta-lines. See https://github.com/sanskrit-lexicon/csl-devanagari/issues/6, https://github.com/sanskrit-lexicon/csl-devanagari/issues/8, https://github.com/sanskrit-lexicon/csl-devanagari/issues/9, https://github.com/sanskrit-lexicon/csl-devanagari/issues/10

## 04 September 2021

## 05 September 2021

## 06 September 2021

1. Added the missing data as suggested by ?? marks in various dictionaries. See https://github.com/sanskrit-lexicon/CORRECTIONS/issues/92#issuecomment-913174476
2. Removed superfluous `{##}` markup from PW. See https://github.com/sanskrit-lexicon/csl-devanagari/issues/16.
3. Removed superfluous `{##}` markup from PWG. See https://github.com/sanskrit-lexicon/csl-devanagari/issues/17.

## 07 September 2021

1. csl-devanagari - Wrote a script `carry_changes_to_cslorig.sh` to carry changes made in csl-devanagari/v02/dictcode/dictcode.txt file to csl-orig/v02/dictcode/dictcode.txt file.
2. csl-orig - INM - changed Varuna to Varuṇa. See https://github.com/sanskrit-lexicon/csl-orig/issues/612.

## 08 September 2021

1. csl-json - Mr. Neelesh Bodas of https://ashtadhyayi.com/ confirmed that the website uses data directly from csl-json repository. It is realtime. Thus, the downstream users who use https://ashtadhyayi.com/ for searching Sanskrit dictionaries get benefits of latest data from Cologne. See https://github.com/sanskrit-lexicon/csl-json/issues/5#issuecomment-914911576 for details.
2. csl-orig - GST - Add lang tag. See https://github.com/sanskrit-lexicon/csl-orig/issues/610.

## 09 September 2021

1. csl-orig - BEN dictionary ab and ls markup preparation made.

## 10 September 2021

1. csl-orig - BEN dictionary ab and ls markup made. See https://github.com/sanskrit-lexicon/BEN/issues/2 for details.

## 11 September 2021

## 12 September 2021

1. cologne-stardict - Removed dependency of `make_babylon.py` script on `lxml` module. lxml is difficult to install on windows, and is an overkill in the context. The script was modified to use native python xml.etree module.
2. csl-orig - GRA dictionary. Added `<ab>` markup for Fi., Ku., BR., Be. SV. gl., Be. SV. gloss., Be. See https://github.com/sanskrit-lexicon/csl-orig/issues/616 and https://github.com/sanskrit-lexicon/GRA/issues/18 for details.


## 13 September 2021

1. csl-devanagari - An error crept into indic-transliteration package which converted `1/6` in slp1 encoding to `१꣡६` in Devanagari encoding. Raised the issue at https://github.com/indic-transliteration/indic_transliteration_py/issues/68 . This bug has resulted in alteration in many dictionaries. Keeping them on hold till the correction happens.
2. sanskrit-lexicon-scans - KRM - scan page is cut at one location. Jim suggested that someone can look at all the scan pages and decide the pages which are sub par. See https://github.com/sanskrit-lexicon-scans/krm/issues/1#issuecomment-917718003

## 14 September 2021

1. csl-homepage - Homepage now shows version number at two places i.e. in header and in bibliographic reference. See https://github.com/sanskrit-lexicon/csl-homepage/issues/9. Also see https://github.com/sanskrit-lexicon/csl-orig/issues/6#issuecomment-907084632 .
2. csl-homepage - AP90 and AE dictionary year of publication was goofed up earlier. Correction made. See https://github.com/sanskrit-lexicon/csl-homepage/issues/6.
3. csl-homepage - CLARIN tooltip correction made. See https://github.com/sanskrit-lexicon/csl-homepage/issues/10.
4. csl-orig - GST - Advertisement of the books of author is moved out of csl-orig/v02/gst/gst.txt file and put at csl-orig/v02/gst/gst_advertisement.txt file. See https://github.com/sanskrit-lexicon/csl-orig/issues/611 for details.
5. sanskrit-lexicon/BOR - new repository BOR started. It is being used to track development of various improvements specific to BOR dictionary.

## 15 September 2021

1. GreekInSanskrit - Greek text for BOESP has been provided. https://github.com/sanskrit-lexicon/GreekInSanskrit/issues/33
2. GreekInSanskrit - Greek texts for BHS, GST and VEI have been provided. See issues https://github.com/sanskrit-lexicon/GreekInSanskrit/issues/37, https://github.com/sanskrit-lexicon/GreekInSanskrit/issues/38 and https://github.com/sanskrit-lexicon/GreekInSanskrit/issues/40.

## 16 September 2021

## 17 September 2021

## 18 September 2021

## 19 September 2021

## 20 September 2021

## 21 September 2021

## 22 September 2021

## 23 September 2021

## 24 September 2021

## 25 September 2021

## 26 September 2021

## 27 September 2021

## 28 September 2021

## 29 September 2021

## 30 September 2021



# Brewing ideas

1. Make line markers uniform across dictionaries. See https://github.com/sanskrit-lexicon/csl-devanagari/issues/26 . 
2. SCH has many double spaces. Need to convert to single space. See https://github.com/sanskrit-lexicon/csl-devanagari/issues/27#issuecomment-913587330.
3. Do jihvAmUlIya and upadhmAnIya require different encoding? See https://github.com/sanskrit-lexicon/csl-devanagari/issues/29 .
4. Add ab,ls tags for GRA (and may be other dictionaries too). See https://github.com/sanskrit-lexicon/GRA/issues/18 .
5. Remove non-Devanagari markup outside scope of `{##}` tags. See https://github.com/sanskrit-lexicon/csl-devanagari/issues/10
6. A cronjob for Cologne jobs. Jim is not yet convinced about the utility or safety of this approach. See https://github.com/sanskrit-lexicon/csl-homepage/commit/830689231db8e12164cdf8cf9f82fbdf16e43d50.
7. PDF download to be made more accessible. See https://github.com/sanskrit-lexicon/COLOGNE/issues/367
8. Compare the IAST and Devanagari headwords in the dictionaries BEN, BUR, MD, MW72, MW and PD. See https://github.com/sanskrit-lexicon/COLOGNE/issues/180 for details.

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
9. sanskrit-lexicon-scans
10. csl-corrections
11. CORRECTIONS
12. COLOGNE
13. Dictionarywise repositories for the following dicts. 
`acc ae ap ap90 ben bhs bop bor bur cae ccs gra gst ieg inm krm mci md mw mw72 mwe pd pe pgn pui pw pwg sch shs skd snp stc vcp vei wil yat lan armh`


# kaz-parallel-corpora

The products have to use on base of Creative Commons licences, exactly, CC BY-SA (CC Attribution-Share Alike)

Developed bilingual tools for crawling and cleaning the corpus are following:
1) URL collection tool;
2) News crawling tools;
3) Data cleaning tool;
4) Sentence splitting tool;
5) Bilingual Frequency Lexicon;
6) Hunalign adapted for Kazakh-English language pair;
7) Morphological segmentation tools;


# Content of the repository

- **compare/** - code to compare the corpus with other parallel corpora
- **corpus/** - corpus files in *.tsv
- **utils/** - scripts used for crawling and cleaning the corpus

# What it needed
●	Python3(version 3.6 or later)

●	lxml

●	sacremoses

●	jupyter 

●	numpy

●	matplotlib

# How it works
utils/ directory consist of developed bilingual tools for crawling and cleaning the Kazakh-English(vise versa) parallel corpora. It consist following files:
●	_clean_text_in_files.sh

●	_gen_langs_lists.py

●	_join_similar_urls.py

●	align_files.py

●	clean_alphabets.py

●	clean_text.py

●	combine_texts_into_one_file.py

●	en_kz.dic

●	extract_data_from_xml.py

●	sacre_norm_tok.py

●	segment.py

●	split_direct_speech.py

●	split_sentences_eng.py

●	split_sentences_kaz.py

●	split_text_into_many_files.py

The sequence of steps for launching files is as follows:
1.	URL collection tool. Run ‘_gen_langs_lists.py’, which collects urls of pages in the language in which the most news is published. 
2.	Collecting news tools. ‘_join_similar_urls.py’ concatenate  similar URL addresses. Collects resources from a list of URLs in .xml format. 
3.	‘extract_data_from_xml.py’ file extract text from xml files and  and save texts into separate file pairs
4.	By ‘split_text_into_many_files.py’ file, each file is saved by the corresponding numbering and the corresponding markup of the language, for example, 1000.kk, 1000.en The file consists of a section, article title, publication date and article text.
5.	Run ‘align_files.py’, that checks an equal number of files in both lists and correspondence of files names to each other.
6.	Data cleaning tools.  Run these ‘split_direct_speech.py’, ‘clean_alphabets.py’, ‘clean_text.py’ files. ‘clean_alphabets.py’ file cleans and replaces incorrect letters, punctuation, unwanted symbols in text/file. ‘_clean_text_in_files.sh’ scripts cleans each language file by using ‘clean_text.py’ and saving output files .
7.	Sentence splitting tools. Run ‘split_sentences_eng.py’ for splitting sentences in case English text, and ‘split_sentences_kaz.py’ for Kazakh text.
8.	Run ‘combine_texts_into_one_file.py’ file, that collects all files into one.
9.	Sacre moses tool. Run ‘sacre_norm_tok.py’ file, that normalizes punctuation and tokenize text.
10.	Bilingual Frequency Lexicon. ‘en_kz.dic’ dictionary file, whose content has the following format as example: may @ мамыр.
11.	Adapted Hunalign aligns bilingual texts on the sentence level. The input files are tokenized and sentence-segmented text in two languages.
12.	 Morphological segmentation tool. Run ‘segment.py’ file to segment Kazakh text to stems and endings splitted by symbol @@. For segmentation, it needed two files: endings file and stopwords. Stopwords file consists of word stems that have been compiled to avoid incorrect, incorrect segmentation. 

With the developed tools, parallel corpora for the Kazakh-English(vice versa) language pair were collected and processed, the results of which are presented in the table below. 

Parallel Kazakh-English corpus collected from news sections of government websites.


# Corpus size

| # | Web-site                  | Number of<br />sentence pairs
| - | ------------------------- | -----------------------------:
| 1 | http://www.akorda.kz/     |  35&nbsp;368
| 2 | https://primeminister.kz/ |   6&nbsp;323
| 3 | http://www.mfa.gov.kz/    |   9&nbsp;152
| 4 | http://economy.gov.kz/    |   6&nbsp;123
| 5 | https://strategy2050.kz/  | 203&nbsp;665
| 6 | News titles               |  41&nbsp;899
|   | **Total:**                | **302&nbsp;530**


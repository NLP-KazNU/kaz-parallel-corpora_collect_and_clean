параллельный двуязычный казахско-английский корпус собранный с текстов новостных разделов сайтов государственных органов

subject domain - news sections of government bodies websites

новостных разделов сайтов государственных органов

Kazakh-English KazNU Corpus (KEKC)


# Технология создания открытого казахско-английского параллельного корпуса
# Technology to create open Kazakh-English parallel corpus
# Technology for creation of open Kazakh-English parallel corpus
# A set of tools that help for creation of parallel Kazakh-English corpora

# Открытый казахско-английский параллельный корпус
# Open Kazakh-English parallel corpus

## Abstract

The main idea of this paper is: we want to propose a way to collect a notable amount of parallel Kazakh-English corpora with good quality in both texts and alignment and as little manual operations as possible.

In this paper, the authors present a new linguistic resource - open Kazakh-English parallel corpus. We describe the problems encountered during our previous work on collecting parallel corpora, techniques, and software that we used to solve those problems, and results that we received.

## 1 Introduction

Corpora is a basis for a lot of linguistic research. Since Kazakh is still considered to be a low resourced language, the creation of new corpora is a very important task for the language. The main idea of this paper is to describe a technology (software) that allows collecting, cleaning, and aligning large amounts of texts from official multilingual web sites with as little manual work as possible. Our goal was to produce such technology and apply it for the creation of open Kazakh-English parallel corpus. In the course of our work we encountered a number of problems and questions:

* which sources to use for collecting presumably parallel texts;
* how to improve the quality of the texts;
* how to minimize efforts for text alignment;
* how to maximize the number of aligned sentences in the result.

// Describe the problem

Kazakh is an under-resourced language. The situation with linguistic resources gets better with every year. But it seems like it does not improve quickly enough. There are some projects aimed at creation of resources ...(привести список с ссылками)... but parallel corpora with Kazakh as one of the languages are not many. (list, enu, wmt, ?) Our previous attempt at the creation of parallel Kazakh-English corpora using the Internet as a source of raw data [ссылка на предыдущую статью] revealed the following difficulties:

- low quality of texts;
- a mix of languages in texts;
- alignment problems;
- manual validation.

By the low quality of texts, we mean several things. First, texts in the Kazakh part of the Internet, for the most part, are initially written in Russian and then get translated into English and Kazakh. That can be seen when analyzing a number of publications on multilingual web-sites: Russian publications are the most numerous, then come English ones and publications in Kazakh are a little behind publications in English. That leads to the fact that content in English and Kazakh has slightly worse quality in terms of style and completeness. Second, when typing in different languages people for some reason use unusual keyboard layouts. In English texts, one might find characters from other alphabets that look similar to English letters or non-printing characters (zero-width spaces, soft hyphens and so on). Symbols like that are the source of confusion during alignment.

By a mix of languages in texts we mean situations when text is written in such a way that it contains parts in different languages (addressing different parts of the audience, quotes, or incomplete translations). Such cases also make alignment more difficult.

Alignment problems were caused not only by described difficulties but also by software. We used (and still use) hunalign ...[ссылка]... for alignment and it has its limitations. The quality of alignment depends very much on the presence of ...bilingual vocabulary... (найти точный термин). When it is missing hunalign creates one using provided texts based on internal heuristics, but for languages that have different linguistic characteristics (which is the case with Kazakh and English) the created file is not even a good one. That causes misalignments and unnecessary grouping of sentences.

Described problems were the reason for manual validation of parallel data that was obtained in [ссылка на предыдущую статью] which is a very time-consuming process.

// State your contributions

In order to deal with described difficulties we have adopted a number of techniques and created a set of scripts that helped to produce a notable amount of parallel Kazakh-English corpora:

- we have identified a good source of parallel texts in Kazakh and English (section 2.1);
- we have created scripts that not only crawl all text from the given ULRs, but also get their translations using corresponding links from the web-page and connecting each pair of translations to each other (section 2.2);
- we have created scripts that clean texts in an interactive mode which does not completely eliminate manual work, but seriously reduces it (section 2.3);
- we have created ...(bilingual vocabulary)... based on word frequency list for crawled texts and grammar of Kazakh and English that very much improves the quality of hunalign's output (section 2.4);
- we have created scripts for the post-processing of parallel sentences (section 2.5).

The techniques and scripts are described in the following sections. The code and corpora are available on ...(ссылка на github)...

## 2 Techniques and scripts used for collecting parallel corpora

### 2.1 Source of quality parallel texts

The problem with quality parallel texts was described above in section 1. In the Republic of Kazakhstan, there are some opportunities to partly solve the problem. For several years now the government has been actively promoting a policy of trilingualism ...(поискать какую-нибудь ссылку)... . All government bodies are expected to publish their materials in three languages: Kazakh, Russian, and English. Judging by the quality of translations it seems like they also have been recruiting people who either studied or lived abroad. Every government website has a news section that updates regularly. And as the news from government websites are published for wide distribution crawling them for computer linguistic purposes should not cause any copyright problems.

In our work we have used following web-sites:
- ...(привести список сайтов с официальными названиями)...

...(привести статистику новостей по сайтам)...

### 2.2 Crawling of parallel texts

When crawling web pages with news we need to keep in mind that we should not download all publications in one language separately from publications in the second language. If we do that, we will end up with two large sets of texts of different sizes without obvious relations between them. We would not be able to find which sentence groups on one side correspond to which sentence groups on the other side. That might cause problems with alignment later. To avoid such problems we downloaded texts in pairs - news item in one language and its translation into the other language. On most sites pages contain a direct link to the same content in the other language. If for some reason there was just a link to the main page in the other language, without direct link to the particular publication we used approach with downloading all materials in different languages separately.

(нарисовать блок-схему)

Crawling was performed in two steps:

- collecting URLs for news items in English;
- gathering data from the collected URLs and from Kazakh pages that correspond to the collected English pages.

For crawling parallel web-pages we have tried using several python libraries: Scrapy ...[привести ссылку]..., Beautiful Soup ...[привести ссылку]..., Requests-HTML. All of them are up to the task. By default, Scrapy works asynchronously, and that makes it difficult to fetch pairs of pages as the order of requests is not obvious at once. Beautiful Soup and Requests-HTML allow more low-level control over request order. For crawling parallel texts we used Requests-HTML. Each publication was saved into its own xml-file with the structure shown in figure ... Pairs of publications that are translations of each other are named in a similar manner using integer identifiers.

figure ... - Structure of xml-file with downloaded content

From each news item, we collected news title, date published, subject section (if it was present), and news text. Titles are usually translated exactly, and that gives a certain number of already aligned sentences. The texts, unfortunately, have to be processed further.

Code that performs crawling is published on ... github ... (добавить ссылку) But it is advised not to use it regularly and during work-time hours of the agencies, whose web-sites are being crawled (or more generally during daytime in UTC+6), as it might slow down their services.

### 2.3 Cleaning of crawled texts

We got a number of *.xml files from the previous step. Before cleaning text we had to extract it from *.xml format int *.txt format. It is done in the following steps:

1. getting file names;
2. sorting file names (as we used integer identifiers when saving the crawling result, sorting puts pairs of files on different languages together);
3. extracting title and text from each file pair:
3.1. if titles in both languages exist they are written into separate files;
3.2. if texts in both languages exist they are written into separate files.

As a result, we got an aligned pair of files with titles and many pairs of files with texts.

To do the cleaning we combined all files with texts in each language into one file, but marking borders of each file, so they can be split back later.

Cleaning focuses on the following:
1. Spaces:
1.1. Zero-width characters (here are the UNICODE codes for characters zero-width that are removed: \u2060, \u2061, \u2062, \u2063, \u180E, \u200B, \u200C, \u200D, \uFEFF, \u00AD).
1.2. Unnecessary leading, trailing spaces and several sequential spaces in the middle of lines.
2. Empty lines.
3. Quotation_marks: various quotation marks («»„“”‘’„”‟❝❞⹂〝〞〟＂) are converted into (").
4. Hyphens: various hyphens (‐− ‒ ⁃ – — ―) are converted into (-).
5. Characters that are not from the text's primary alphabet. As there are many cases when using English characters in Kazakh texts and vice-versa is correct (organization names, person names, special terminology, etc.) this task cannot be automated and has to be performed manually using search with regular expressions. There are several strategies used one after another in order to reduce the amount of manual work:
5.1. Check for easily confused characters: (АВҒЕКМНОРСТУҮХҺІЬаеорсуүхһі) from the Kazakh alphabet and (ABFEKMHOPCTYXhIbaeopcyxhi) from the English alphabet.
5.2. Check every word that has mixed characters from different alphabets.
5.3. Check all symbols that are not usually expected in Kazakh of English texts - symbols that are not Kazakh or English letters, punctuation marks, spaces, numbers, currency symbols, etc.
6. Spaces - this step needs to be repeated as previous steps could add more unnecessary leading, trailing spaces and several sequential spaces in the middle of lines.

(нарисовать блок-схему)

After the cleaning, we split the texts into sentences. There are tools that can automate this splitting, but our tests showed that they work only in general cases and additional trained is needed in order for them to work better with particular texts. As we did not have labeled training data for sentences splitting, we decided to do it semi-manually. We wrote a script that splits the text into sentences at every period that is preceded with five letters in Kazakh texts and four letters in English texts. Cases, where a period is preceded with fewer letters, had to be checked manually. Then we checked for cases where a period is preceded with or followed by a non-alphabet character with following patterns: (".), (."), ('.), (.'), (%.), ( ). ), (<number>.), (<non-space characters>.<space><non-space characters>), (.<space><uppercase character>). Sentences that end with an exclamation mark and a question mark are usually very few and found and split in no time

Unfortunately, that is the most laborious part of the work, but it is very important for getting aligned sentences. So after splitting was done we did some checks in order to make sure, that there were no errors added during sentence splitting. We checked for URLs and e-mail addresses; sentences that start with lowercase letters; sentences that do not end with (.), (!) or (?); and lines that are relatively short (shorter than 30-40 characters).

After that we received 2 files that contained a single sentence on each line.

### 2.4 Improving alignment quality

In order to improve alignment quality, we took the following steps. Using sacremoses library (... добавить ссылку ...) we normalized punctuation and tokenized texts. After that we lowercased both files and created word frequency lists for English and Kazakh texts. Even though word frequency list for Kazakh without taking morphological segmentation into account usually useless, it helps to identify words and word forms most used in texts. For each website, we considered approximately 100 most used words from each side. If there were words corresponding to each other we took from frequency lists the word from the English side and all word forms of the word from the Kazakh side. Kazakh has a very rich morphology so it is a very common situation when one English word form can correspond to several dozens Kazakh word forms as translations in different circumstances. But hunalign does not take different word forms into account by default. So adding them into (... Dictionary file ...) noticeably improves alignment results. Altogether we have collected ... (указать итоговый размер словаря hunalign ...) word form pairs. It can be found in the corpus repository (... указать ссылку на файл со словарём ...). We have to note that applying morphological segmentation to Kazakh texts has the potential of further improving the segmentation. And we have plans to experiment with it in the future.

The files are then divided into original parts containing separate news items, using border marks mentioned in section 2.3. After that, each file pair is aligned with hunalign and (... hunalign dictionary file ...) and results of each alignment are combined into one file in *.tsv format.

### 2.5 Post-processing of parallel sentences

Post-processing of parallel sentences consists of the following steps:
1. Check pairs with extremely low hunalign score and remove them if they are misaligned.
2. Remove duplicate sentences pairs.
3. Shuffle remaining sentences pairs.

## 3 Results

We have applied all the techniques described in sections 2.2-2.5 to the websites listed in section 2.1. The results are shown in the table ...

(... таблица с результатами ...)

Our parallel corpus contains:
- ... sentence pairs;
- ... Kazakh words;
- ... English words.

## 4 Related works

## 5 Conclusions and further work

In the paper we have described a way to collect notable amount of parallel Kazakh-English corpora with good quality in both texts and alignment. Although we tried to automate as much tasks as possible the quality of texts and alignment still requires some considerable amount of manual operations. But compared to our previous attempt at creating parallel Kazakh-English corpus the techniques used in this work prove to be much more effective.
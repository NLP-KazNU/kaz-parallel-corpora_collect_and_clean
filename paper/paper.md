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

The main idea of this paper is : we want to propose a way to collect notable amount of parallel Kazakh-English corpora with good quality in both texts and alignment and as little manual operations as possible.

In this paper authors present new linguistic resource - open Kazakh-English parallel corpus. We describe problems encountered during our previous work on collecting parallel corpora, techniques and software that we used to solve those problems, and results that we received.

## 1 Introduction

Corpora is a basis for many linguistic research. Since Kazakh is still considered to be a low resourced language, creation of new corpora is a very important task for the language. The main idea of this paper is to describe a technology (a software) that allows collecting, cleaning, and aligning large amounts of texts from official multilingual web sites with as minimum manual work as possible. Our Goal was to produce such technology and apply it for creation of open Kazakh-English parallel corpus. In the course of our work we encountered a number of problems and questions:

* which sources to use for collecting presumably parallel texts;
* how to improve quality of the texts;
* how to minimize efforts for text alignment;
* how to maximize the number of aligned sentences in the result.

// Describe the problem

Kazakh is under resourced language. The situation with linguistic resources gets better with every year. But it seems like it does not improve quickly enough. There are some projects aimed at creation of resources ...(привести список с ссылками)... but parallel corpora with Kazakh as one of the languages are not many. (list, enu, wmt, ?) Our previous attempt at creation of parallel Kazakh-English corpora using the Internet as a source of raw data [ссылка на предыдущую статью] revealed following difficulties:

- low quality of texts;
- mix of languages in texts;
- alignment problems;
- manual validation.

By low quality of texts we mean several things. First, texts in the Kazakh part of the Internet for the most part initially written in Russian and then get translated into English and Kazakh. That can be seen when analyzing number of publications on multilingual web-sites: Russian publications are the most numerous, than come English ones and Kazakh publications are a little behind English publications. That leads to the fact that content in English and Kazakh has slightly worse quality in terms of style and completeness. Second when typing in different languages people for some reason use unusual keyboard layouts. In English texts there one might find characters from other alphabets that look similar to English letters or non-printing characters (zero-width spaces, soft hyphens and so on). Symbols like that are the source of confusion during alignment.

By mix of languages in texts we mean situations when text is written in such way that it contains parts in different languages (addressing different parts of the audience, quotes, or incomplete translations). Such cases also make alignment more difficult.

Alignment problems were caused not only by described difficulties but also by software. We used (and use) hunalign ...[ссылка]... for alignment and it has its limitations. The quality of alignment depends very much on presence of ...bilingual vocabulary... (найти точный термин). When it is missing hunalign creates one from provided texts based on internal heuristics, but for languages with different linguistic characteristics (which is the case with Kazakh and English) the created file is not even a good one. That causes misalignments and unnecessary grouping of sentences.

The described problems were the reason for manual validation of parallel data that was obtained in [ссылка на предыдущую статью] which is a very time consuming process.

// State your contributions

In order to to deal with described difficulties we have adopted a number of techniques and created a set of scripts that helped to produce a notable amount of parallel Kazakh-English corpora:
- we have identified a good source of parallel texts in Kazakh, English and Russian (section 2.1);
- we have created scripts that not only crawl all text from the given ULRs, but also get their translations using corresponding link from the web-page and connects each pair of translations to each other (section 2.2);
- we have created scripts that clean texts in interactive mode which does not completely eliminate manual work, but seriously reduces it (section 2.3);
- we have created ...(bilingual vocabulary)... based on word frequency list for crawled texts and grammar of Kazakh and English that greatly improves the quality of hunalign's output (section 2.4);
- we have created scripts for post-processing of parallel sentences (section 2.5).

The techniques and scripts are describe in following sections. The code and corpora are available on ...(ссылка на github)...

## 2 Techniques and scripts used for collecting parallel corpora

### 2.1 Source of quality parallel texts

The problem with quality parallel texts was described above in section 1. In the Republic of Kazakhstan there are some opportunities to partly solve the problem. For several years now the government has been actively promoting a policy of trilingualism ...(поискать какую-нибудь ссылку)... . All government bodies are expected to publish their materials in three languages: Kazakh, Russian, and English. Judging by the quality of translations it seems like they also have been recruiting people who either studied or lived abroad. Every government web-site has a news section that updates regularly. And as te news from government web-sites are published for wide distribution crawling them for computer linguistic purposes should not cause any copyright problems.

In our work we have used following web-sites:
- ...(привести список сайтов с официальными названиями)...

...(привести статистику новостей по сайтам)...

### 2.2 Crawling of parallel texts

When crawling web pages with news we need to keep in mind that we should not download all publications in one language separately from publications in the second language. If we do that, we will end up with two large sets of texts of different size without obvious relations between them. We would not be able to find which sentence groups on one side correspond to which sentence groups on the other side. That might cause problems with alignment later. To avoid such problems we downloaded texts in pairs - news item in one language and its translation into the other language. On most sites pages contain direct link to the same content in the other language. If for some reason there was just a link to a main page in the other language, without direct link to the particular publication we used approach with downloading all materials in different languages separately.

For crawling parallel text we have tried using several python libraries: Scrapy ...[привести ссылку]..., Beautiful Soup ...[привести ссылку]..., Requests-HTML. All of them are up to the task. By default Scrapy works asynchronously, and that makes it difficult to fetch pairs of pages as order of requests is not obvious at once. Beautiful Soup and Requests-HTML allow more low-level control over request order. for crawling of parallel texts we used Requests-HTML. Each publication was saved into is own xml-file with structure shown in figure ... Pairs of publications that are translations of each other are named in similar manner using integer id's.

figure ... - Structure of xml-file with downloaded content

From each news item we collected news title, date published, subject section (if it was present), and news text. Titles are usually translated exactly, and that gives a certain number of already aligned sentences. The texts unfortunately have to be processed further.

### 2.3 Cleaning of crawled texts

### 2.4 Improving alignment quality

### 2.5 Post-processing of parallel sentences

## 3 Results

## 4 Related works

## 5 Conclusions and further work

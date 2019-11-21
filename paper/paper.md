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

### 2.2 Crawling of parallel texts

### 2.3 Cleaning of crawled texts

### 2.4 Improving alignment quality

### 2.5 Post-processing of parallel sentences

## 3 Results

## 4 Related works

## 5 Conclusions and further work

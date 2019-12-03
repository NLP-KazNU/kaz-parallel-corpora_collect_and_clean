#!/usr/bin/env bash

cd ./kz-en/

scrapy runspider ./mfa_gov_kz_news_en_spider.py \
    -s JOBDIR=../scrapy_job_dir_1 \
    -o "./mfa_gov_kz_news_(kz-en)_en.xml"

scrapy runspider ./mfa_gov_kz_news_kz_spider.py \
    -s JOBDIR=../scrapy_job_dir_2 \
    -o "./mfa_gov_kz_news_(kz-en)_kz.xml"

cd ../kz-ru/

scrapy runspider ./mfa_gov_kz_news_kz_spider.py \
    -s JOBDIR=../scrapy_job_dir_3 \
    -o "./mfa_gov_kz_news_(kz-ru)_kz.xml"

scrapy runspider ./mfa_gov_kz_news_ru_spider.py \
    -s JOBDIR=../scrapy_job_dir_4 \
    -o "./mfa_gov_kz_news_(kz-ru)_ru.xml"
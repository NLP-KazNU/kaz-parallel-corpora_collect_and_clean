#!/usr/bin/env bash

cd ./kz-en/

scrapy runspider ./economy_gov_kz_news_en_spider.py \
    -s JOBDIR=../scrapy_job_dir_1 \
    -o "./economy_gov_kz_news_(kz-en)_en.xml"

cd ../kz-ru/

scrapy runspider ./economy_gov_kz_news_kz_spider.py \
    -s JOBDIR=../scrapy_job_dir_2 \
    -o "./economy_gov_kz_news_(kz-ru)_kz.xml"

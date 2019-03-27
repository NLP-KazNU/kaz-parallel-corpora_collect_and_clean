#!/usr/bin/env bash

cd ./kz-en/

# scrapy runspider ./primeminister_kz_news_en_spider.py -o "./primeminister_kz_news_(kz-en)_en.xml"

# scrapy runspider ./primeminister_kz_news_kz_spider.py \
    # -s JOBDIR=../scrapy_job_dir_1 \
    # -o "./primeminister_kz_news_(kz-en)_kz.xml"

cd ../kz-ru/

scrapy runspider ./primeminister_kz_news_kz_spider.py \
    -s JOBDIR=../scrapy_job_dir_2 \
    -o "./primeminister_kz_news_(kz-ru)_kz.xml"

scrapy runspider ./primeminister_kz_news_ru_spider.py \
    -s JOBDIR=../scrapy_job_dir_3 \
    -o "./primeminister_kz_news_(kz-ru)_ru.xml"

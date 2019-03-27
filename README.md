# kaz-parallel-corpora

## Заметки

Variable needed for json-encoding to be utf-8
```shell
FEED_EXPORT_ENCODING='utf-8'
```

"Сonventional" way to run crawling. Used when there is a crawling project.
```shell
scrapy crawl quotes -o quotes.json
```

Способ запускать краулинг, имея файла с описанием "паука", без создания проекта краулинга.
```shell
scrapy runspider <spider_file.py> -o <output.json>
```

```shell
FEED_EXPORT_ENCODING='utf-8' scrapy runspider primeminister_kz_news_urls_ru_spider.py -o primeminister_kz_news_urls_ru.json
```

## Последовательность действий по сбору параллельного корпуса

1. Собрать url-ы страниц на языке, на котором опубликовано больше всего новостей (чаще всего, это русский язык).
```
FEED_EXPORT_ENCODING='utf-8' scrapy runspider <spider_file.py> -o <output_file.json>
```
2. Из файла с url-ами сгенерировать списки урлов с новостями на 3 языках.
TODO: Написать скрипт: ввод - файл с предыдущего шага; вывод - 3 текстовых файла.

## TODO:
- описать процесс "установки" проекта, начиная с pipenv
- xmllint
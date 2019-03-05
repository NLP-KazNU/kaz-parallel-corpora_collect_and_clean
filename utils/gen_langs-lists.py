#!/usr/bin/env python3
#
# скрипт, генерирующий 3 списка с url-ами, которые отличаются только указанием языка - /kz/, /ru/, /en/
# ввод - файл *.json
# TODO: описать ожидаемую структуру json
# вывод - 3 текстовых файла: <site>_urls_kz.txt, <site>_urls_ru.txt, <site>_urls_en.txt

# docopt
# -input, -i - input file (*.json)
# -input_language, -lang [kz|ru (default)|en]
# прочитать json с url-ами на одном языке в список
# сгенерировать 2 списка с url-ами на оставшихся языках
# записать каждый из списков в свой файл: <site>_urls_kz.txt, <site>_urls_ru.txt, <site>_urls_en.txt
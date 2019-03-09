#!/usr/bin/env python3
#
# script generates 3 lists with urls that differ only with language indication -
# /kz/, /ru/, /en/
#
# input - *.json file
# expected json structure:
#   [
#       {"url": "https://..."},
#       {"url": "https://..."},
#       ...
#       {"url": "https://..."}
#   ]
#
# output - 3 text files: <site>_urls_kz.txt, <site>_urls_ru.txt, <site>_urls_en.txt

# docstring for docopt
"""gen_langs_lists.py

Usage:
    gen_langs_lists.py (-i | --input) <file_with_urls>
    gen_langs_lists.py (-h | --help)
    gen_langs_lists.py (-v | --version)

Options:
    -h --help       Show this screen.
    -v --version    Show version.
    -i --input      path to a file with crawled urls (json)
"""

from docopt import docopt
import json
import re


def gen_list_and_file(
    url_list: list, file_name: str, change_from: str = "", change_to: str = ""
) -> None:
    """
    Accepts a list of urls, substitute language indication in all urls to given value,
    and prints the result into a file with provided file_name.
    """
    with open(file_name, "w") as urls_file:
        for url in url_list:
            print(url.replace(change_from, change_to), file=urls_file)


def main():
    # read json with urls into a list
    file_with_urls = arguments["<file_with_urls>"]
    with open(file_with_urls, "r") as json_data:
        urls_dict = json.load(json_data)

    urls = []
    for item in urls_dict:
        urls.append(item["url"])

    # extract a site name from the first url
    site = re.search(pattern="\w+\.kz", string=urls[0]).group(0)

    # generate url lists in all 3 languages
    # save each list into its own file: <site>_urls_kz.txt, <site>_urls_ru.txt,
    # <site>_urls_en.txt
    # if input urls contain indication for Russian (/ru/)
    # generate /ru/, /kz/, /en/
    if "/ru/" in urls[0]:
        gen_list_and_file(url_list=urls, file_name=site + "_urls_ru.txt")
        gen_list_and_file(
            url_list=urls,
            file_name=site + "_urls_kz.txt",
            change_from="/ru/",
            change_to="/kz/",
        )
        gen_list_and_file(
            url_list=urls,
            file_name=site + "_urls_en.txt",
            change_from="/ru/",
            change_to="/en/",
        )
    # if input urls contain indication for Kazakh (/kz/)
    # generate /kz/, /ru/, /en/
    elif "/kz/" in urls[0]:
        gen_list_and_file(url_list=urls, file_name=site + "_urls_kz.txt")
        gen_list_and_file(
            url_list=urls,
            file_name=site + "_urls_ru.txt",
            change_from="/kz/",
            change_to="/ru/",
        )
        gen_list_and_file(
            url_list=urls,
            file_name=site + "_urls_en.txt",
            change_from="/kz/",
            change_to="/en/",
        )
    # if input urls contain indication for English (/en/)
    # generate /en/, /kz/, /ru/
    elif "/en/" in urls[0]:
        gen_list_and_file(url_list=urls, file_name=site + "_urls_en.txt")
        gen_list_and_file(
            url_list=urls,
            file_name=site + "_urls_kz.txt",
            change_from="/en/",
            change_to="/kz/",
        )
        gen_list_and_file(
            url_list=urls,
            file_name=site + "_urls_ru.txt",
            change_from="/en/",
            change_to="/ru/",
        )


if __name__ == "__main__":
    arguments = docopt(__doc__, version="gen_langs_lists.py v.0.1")
    main()

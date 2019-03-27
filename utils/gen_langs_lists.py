#!/usr/bin/env python3
#
# script generates 2 lists with urls that differ only with language indication -
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
# output - 2 text files: first - for the language used in input file, second - requested one
# (two of the following: <site>_urls_kz.txt, <site>_urls_ru.txt, <site>_urls_en.txt)

# docstring for docopt
"""gen_langs_lists.py

Usage:
    gen_langs_lists.py (-i | --input) <file_with_urls> --lang_from <lang_from> --lang_to <lang_to>
    gen_langs_lists.py (-h | --help)
    gen_langs_lists.py (-v | --version)

Options:
    -i --input      path to a file with crawled urls (json)
    --lang_from     language indication used in input file
    --lang_to       requested second language indication
    -v --version    Show version.
    -h --help       Show this screen.
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
            print(
                url.replace("/" + change_from + "/", "/" + change_to + "/"),
                file=urls_file,
            )


def main():
    # collect parameter values
    file_with_urls = arguments["<file_with_urls>"]
    lang_from = arguments["<lang_from>"]
    lang_to = arguments["<lang_to>"]

    # read json with urls into a list
    with open(file_with_urls, "r") as json_data:
        urls_dict = json.load(json_data)

    urls = []
    for item in urls_dict:
        urls.append(item["url"])

    # extract a site name from the first url
    site = re.search(pattern=".+\.kz", string=urls[0]).group(0)
    site = site.replace("https://", "")
    site = site.replace("http://", "")

    # generate url lists in 2 languages
    # save each list into its own file: <site>_urls_kz.txt, <site>_urls_ru.txt, or
    # <site>_urls_en.txt
    if "/" in lang_from:
        lang_from = lang_from.replace("/", "")
    if "/" in lang_to:
        lang_to = lang_to.replace("/", "")
    gen_list_and_file(url_list=urls, file_name=site + "_urls_" + lang_from + ".txt")
    gen_list_and_file(
        url_list=urls,
        file_name=site + "_urls_" + lang_to + ".txt",
        change_from=lang_from,
        change_to=lang_to,
    )


if __name__ == "__main__":
    arguments = docopt(__doc__, version="gen_langs_lists.py v.0.1")
    main()

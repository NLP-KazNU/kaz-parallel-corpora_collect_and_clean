#!/usr/bin/env python3

from requests_html import HTMLSession
from typing import List

# TODO перевести и перенести
# TODO make output to console
# # собрать ссылки на новости (англ)


def get_all_news_page_urls(max_page_num: int) -> List[str]:
    """
    Collect all urls of pages that have links to news pages.
    """
    news_page_urls = []
    for num in range(1, max_page_num + 1):
        news_page_urls.append("http://www.akorda.kz/en/events?page=" + str(num))
    return news_page_urls


def get_all_eng_news_urls(url: str) -> List[str]:
    session = HTMLSession()
    r = session.get(url)
    sel = "div.list-block-title a"
    return [x.attrs["href"] for x in r.html.find(sel)]



if __name__ == "__main__":
    page_urls = get_all_news_page_urls(max_page_num=543)

    news_urls = []
    for page_url in page_urls:
        news_urls.extend(get_all_eng_news_urls(url=page_url))

    with open(file="news_urls.en", mode="w") as result_file:
        for line in news_urls:
            print(line, file=result_file)

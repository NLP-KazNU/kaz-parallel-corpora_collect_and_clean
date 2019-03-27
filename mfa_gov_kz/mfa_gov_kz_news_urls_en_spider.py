import scrapy


class mfa_gov_kz_news_urls_en(scrapy.Spider):
    name = "mfa_gov_kz_news_urls_en"
    start_urls = ["http://mfa.gov.kz/en/content/news"]

    def parse(self, response):
        # response.css("div.content-news-item-title a::attr(href)").get()
        # вытаскиваем содержимое тегов <div class="content-news-item-title"> <a...>...</a> </div>
        for url in response.css("div.content-news-item-title a"):
            # вытаскиваем из тегов <a> значение атрибута "href"
            # собираем полный url
            yield {"url": "http://mfa.gov.kz" + url.css("::attr(href)").get()}

        # ищем следующую страницу
        next_page = response.css('li.next a::attr(href)').get()
        # если следующая страница существует, переходим на неё
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
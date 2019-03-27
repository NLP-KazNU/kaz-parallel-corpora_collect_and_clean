import scrapy


class economy_gov_kz_news_urls_en(scrapy.Spider):
    name = "economy_gov_kz_news_urls_en"
    start_urls = ["http://economy.gov.kz/en/news"]

    def parse(self, response):
        # response.css("div.news_body_wrapper div.views-field-title-field div.field-content a::attr(href)").get()
        for url in response.css("div.news_body_wrapper div.views-field-title-field div.field-content a"):
            # вытаскиваем из тегов <a> значение атрибута "href"
            # собираем полный url
            yield {"url": "http://economy.gov.kz" + url.css("::attr(href)").get()}

        # ищем следующую страницу
        next_page = response.css('li.pager-next a::attr(href)').get()
        # если следующая страница существует, переходим на неё
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
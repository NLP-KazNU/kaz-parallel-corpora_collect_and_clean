import scrapy


class primeminister_kz_news_urls_kz(scrapy.Spider):
    name = "primeminister_kz_news_urls_kz"

    def start_requests(self):
        # общее количество страниц с новостями на сайте
        total_news_pages = 1441
        # массив для полного списка url
        # приходится делать так, потому что в пагинации нет ссылок с меткой "next"
        urls = []
        for i in range(total_news_pages + 1):
            urls.append("https://primeminister.kz/kz/news/page/" + str(i))

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # response.css("a.item::attr(href)").get()
        # вытаскиваем содержимое тегов <a class="item">
        for url in response.css("a.item"):
            # вытаскиваем из тегов <a class="item"> значение атрибута "href"
            # собираем полный url
            yield {"url": "https://primeminister.kz" + url.css("::attr(href)").get()}

import scrapy


class primeminister_kz_news_kz(scrapy.Spider):
    name = "primeminister_kz_news_kz"

    def start_requests(self):
        # read urls from a file
        with open("./primeminister.kz_urls_kz.txt") as urls_file:
            urls = urls_file.read().splitlines()

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # url - response.url
        # section - response.css('div.navi a::text').getall()[-1]
        # title - response.css('h1.main-news-item__head::text').getall()
        # date-time - response.css('div.date::text').getall()[0]
        # text - response.css('p::text').getall()

        yield {
            "url": response.url,
            "section": response.css("div.navi a::text").getall()[-1],
            "title": response.css("h1.main-news-item__head::text").getall(),
            "date-time": response.css("div.date::text").getall()[0],
            "text": response.css("p::text").getall(),
        }

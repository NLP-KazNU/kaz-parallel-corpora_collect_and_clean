import scrapy


class mfa_gov_kz_news_ru(scrapy.Spider):
    name = "mfa_gov_kz_news_ru"

    def start_requests(self):
        # read urls from a file
        with open("./mfa.gov.kz_urls_ru.txt") as urls_file:
            urls = urls_file.read().splitlines()

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # url - response.url
        # title - response.css('h4::text').getall()
        # date-time - response.css('div.content-functions-date::text').getall()
        # text - response.css('div.wrap__desc p::text').getall()

        yield {
            "url": response.url,
            "title": response.css('h4::text').getall(),
            "date-time": response.css('div.content-functions-date::text').getall(),
            "text": response.css('div.wrap__desc p::text').getall(),
        }

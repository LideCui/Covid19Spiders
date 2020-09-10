import scrapy
from scrapy_splash import SplashRequest

class Covid19TabletsSpider(scrapy.Spider):
    name = 'covid19_tablets'
    # allowed_domains = ['https://www.canada.ca/en/public-health/']
    start_urls = ['https://health-infobase.canada.ca/covid-19/iframe/table.html']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parse, endpoint='render.html')

    def parse(self, response):
        table=response.xpath('//*[@id="dataTable"]')
        rows=table.xpath('//tbody//tr')
        print(rows)
        yield(rows)

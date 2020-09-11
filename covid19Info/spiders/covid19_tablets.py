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
        for row in response.xpath('//*[@id="dataTable"]//tbody//tr'):
            yield {
                'activeCase': row.xpath('td[2]//text()').extract_first(),
                'activeRate': row.xpath('td[3]//text()').extract_first(), 
            }
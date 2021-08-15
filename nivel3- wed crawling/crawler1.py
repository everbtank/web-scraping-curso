import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class MySpider(CrawlSpider):
    name = 'airbnb.com.pe'
    allowed_domains = ['airbnb.com.pe']
    start_urls = [
        "https://www.amazon.com/IdeaPad-generaci%C3%B3n-i5-1035G1-i7-7500U-Bluetooth/dp/B0981B132N/ref=sr_1_1_sspa?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=laptop&qid=1627398537&sr=8-1-spons&psc=1&smid=A1EC41WMQMGYRA&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExN044SVdHVkxHR1A2JmVuY3J5cHRlZElkPUEwNjk1OTI3MTROWElSSkU5MjlJSyZlbmNyeXB0ZWRBZElkPUEwMjY3NjE3SFdRVFY3M0NPRldWJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==",
        "https://www.amazon.com/-/es/30111/dp/B08HJHP6Y6/ref=sr_1_1?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=xiaomi&qid=1627398575&sr=8-1",
        "https://www.amazon.com/-/es/Pulsera-quilates-ajustable-Amarillo-20A-B01-Y/dp/B082TRCLRN/ref=sr_1_2?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=bracelet&qid=1627398600&sr=8-2"
    ]

    rules = (
        Rule(LinkExtractor(allow=('=ÅMÅŽÕÑ&', )), callback='parse_item'),
    )

    def parse_item(self, response):
        self.logger.info('Hi, this is an item page! %s', response.url)
        item = scrapy.Item()
        item['title'] = response.xpath('//h1[@id="title"]/span/text()').get()
        item['precio'] = response.xpath('//span[@id="priceblock_ourprice"]/text()').get()
        item['especificacion'] = response.xpath('//a[@id="acrCustomerReviewLink"]/span/text()').get()
       
       
        url = response.xpath('//td[@id="additional_data"]/@href').get()
        return response.follow(url, self.parse_additional_page, cb_kwargs=dict(item=item))

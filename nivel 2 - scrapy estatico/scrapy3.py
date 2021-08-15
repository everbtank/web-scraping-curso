
import scrapy

class QuotesSpider(scrapy.Spider):
    name="quotes"
    start_urls=["http://quotes.toscrape.com/author/Marilyn-Monroe/"]
    
    def parse(self,response):
        yield {
            'text': response.xpath('//div[@class="author-description"]/text()').get(),
            'autor': response.xpath('//h3/text()').get(),
            'tags': response.xpath('//span[1]/a[1]/text()').get(),   
        }
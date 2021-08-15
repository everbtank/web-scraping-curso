#Forma recursivada
import scrapy

class QuotesSpider(scrapy.Spider):
    name ='recursiva'
    start_urls=['https://quotes.toscrape.com/page/1/',
                'https://quotes.toscrape.com/page/2/',
                'https://quotes.toscrape.com/page/3/']
    
    def parse(self, response):
        for quote in response.xpath('//div[@class="quote"]'):
           yield{
               'text':quote.xpath('./span[@class="text"]/text()').get(),
               'author': quote.xpath('./span/small[@class="author"]/text()').get(),
                 'tags': quote.xpath('./div[@class="tags"]/a[1]/text()').get(),
           }
        
        next_page =response.xpath('//li[@class="next"]/a').get()
        if next_page is not None:
             next_page = response.urljoin(next_page)
             yield scrapy.Request(next_page,callback=self.parse)
            
            
        


    
     
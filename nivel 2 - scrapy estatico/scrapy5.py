
#FORMA RECURSIVA CON CSS SELECTOR
import scrapy

class QuotesSpider(scrapy.Spider):
    name ='recursiva_selector'
    start_urls=['https://quotes.toscrape.com/page/1/',
                'https://quotes.toscrape.com/page/2/',
                'https://quotes.toscrape.com/page/3/']
    
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield{
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').get(),
     
            }
            
        next_page =response.css('li.next a::attr(href)').get()
        if next_page is None:
            next_page =response.urljoin(next_page)
            yield scrapy.Request(next_page,callback=self.parse)
            
            
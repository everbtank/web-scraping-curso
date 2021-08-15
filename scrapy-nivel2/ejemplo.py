import scrapy

class ScraperHola(scrapy.Spider):
    custom_settings = {
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
      
    }
    name = 'scraper'
    start_urls=['https://mulier.com']
    
    def parse(self,reponse):
        print(reponse.xpath('//div/text()').get())
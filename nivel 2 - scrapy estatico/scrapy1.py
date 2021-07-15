import scrapy

class ScrapyHola(scrapy.Spider):
    custom_settings = {
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',  
    }
    name="scrapy1"
    start_urls=["https://muliier.com/"]
    
    
    def parse(self,response):
        data =response.xpath("//h1/text()").get()
        yield data
        
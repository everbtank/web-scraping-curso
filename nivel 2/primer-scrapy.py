import scrapy

class scraperSipder(scrapy.Spider):
   
   
    name = "spider"
    alloweb_domains=['mercadolibre.com.pe']
    
    start_urls=["https://www.mercadolibre.com.pe/c/celulares-y-telefonos#menu=categories"]

def parse(self, response):
    data=response.xpath('//*[@id="root-app"]/div/div[2]/section/div[1]/h2/text()').get()
    yield data
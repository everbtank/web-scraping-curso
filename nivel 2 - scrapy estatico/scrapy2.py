#SOLICTUDES A URL
import scrapy

class scrapySolictudes(scrapy.Spider):
    name = "muliier"
    start_urls=['https://muliier.com/ropa-femenina/',
        'https://muliier.com/cuidado-personal/']
    
    def parse(self, response):
        page= response.url.split("/")[-2]
        filename = f'categorias-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
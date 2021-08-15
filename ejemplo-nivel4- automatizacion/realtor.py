from scrapy.selector import Selector
from twisted.internet import reactor 
from twisted.internet.task import LoopingCall
from scrapy.crawler import CrawlerRunner
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

   
class RentaCrawler(CrawlSpider):
    name = 'RentaCrawler'
    
    custom_settings = {
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
        'CLOSESPIDER_PAGECOUNT': 20,
        'LOG_ENABLED': True
    }

    
    allowed_domains = ['realtor.com']
 
    start_urls = ['https://www.realtor.com/rentals']
    
    handle_httpstatus_list = [403]

    # Tiempo de espera entre cada requerimiento. Nos ayuda a proteger nuestra IP.
    download_delay = 1
    base_url = 'https://www.realtor.com/'
    DOWNLOADER_MIDDLEWARES = {'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,}

   
    rules = (
        Rule( # Regla de movimiento VERTICAL hacia el detalle de los hoteles
            LinkExtractor(
                allow=r'/realestateandhomes-detail' # Si la URL contiene este patron, haz un requerimiento a esa URL
            ), follow=True, callback="parse_renta"), # El callback es el nombre de la funcion que se va a llamar con la respuesta al requerimiento hacia estas URLs
    )
    
    
 
    # EL RESPONSE ES EL DE LA URL SEMILLA
    def parse_start_url(self, response): 
        sel = Selector(response)
        rentas = sel.xpath('.//div[@data-testid="property-card"]')
        print("Buscando resultados:   ", len(rentas)," encontrados ")


    def parse_renta(self, response):
        
        sel = Selector(response)
        Property_Address=sel.xpath('*//[@id="ldp-address"]/h1/span[1]/text()').get()
        #Property_Street=sel.xpath('*//[@id="ldp-address"]/h1/span[2]/text()').get()
        #city=sel.xpath('*//[@id="ldp-address"]/h1/span[3]/text()').get()
     
        # Guardado de datos en un archivo
        f = open('./excel1.csv', 'a')
       
        #f.write(Property_Address + ","+ Property_Street+","+city + ","+state +","+codezip +","+bed +","+bath +","+total_square +","+ year_build +","+rent_price+","+ sales_price+","+contacto+"\n")
        f.write(Property_Address  +"\n")
        f.close()
        
      
        
        print('Property_Address: '+Property_Address)
        #print('Property_Street: '+Property_Street)
        #print('city: '+city)
      
        print()

        # No necesito hacer yield. El yield me sirve cuando voy a guardar los datos
        # en un archivo, corriendo Scrapy desde Terminal

# Logica para correr una extraccion de Scrapy periodicamente. Es decir, automatizarla.

print("\n========== Crawler Renta ===========\n")
runner = CrawlerRunner()
task = LoopingCall(lambda: runner.crawl(RentaCrawler)) # Para Investigar: Funciones Anonimas en Python
task.start(1) # Tiempo en segundos desde la primera corrida del programa para repetir la extraccion
reactor.run()



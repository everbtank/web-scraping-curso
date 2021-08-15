from scrapy.selector import Selector
from twisted.internet import reactor 
from twisted.internet.task import LoopingCall
from scrapy.crawler import CrawlerRunner
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class RentaCrawler(CrawlSpider):
    name = 'VentaCrawler'
    
    custom_settings = {
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
        'CLOSESPIDER_PAGECOUNT': 20,
        'LOG_ENABLED': True
    }

    
    allowed_domains = ['amazon.com']
 
    #start_urls = ['https://www.realtor.com/rentals','https://www.realtor.com/apartments/New-York_NY','https://www.realtor.com/apartments/Miami_FL','https://www.realtor.com/apartments/Chicago_IL']
    start_urls = ['https://www.amazon.com/s?k=bracelet&__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss']
    handle_httpstatus_list = [403]

    # Tiempo de espera entre cada requerimiento. Nos ayuda a proteger nuestra IP.
    download_delay = 1
    base_url = 'https://www.amazon.com/'
  

   
    rules = (
        Rule( # Regla de movimiento VERTICAL hacia el detalle de los hoteles
            LinkExtractor(
                allow=r'=ÅMÅŽÕÑ&' # Si la URL contiene este patron, haz un requerimiento a esa URL
            ), follow=True, callback="parse_renta"), # El callback es el nombre de la funcion que se va a llamar con la respuesta al requerimiento hacia estas URLs
    )
    
    
 
    # EL RESPONSE ES EL DE LA URL SEMILLA
    def parse_start_url(self, response): 
        sel = Selector(response)
        rentas = sel.xpath('.//div[@data-component-type="s-search-result"]')
        print("Buscando resultados:   ", len(rentas)," encontrados ")


    def parse_renta(self, response):
        
        sel = Selector(response)
        titulo = response.xpath('//h1[@id="title"]/span/text()').get()
        precio = response.xpath('//span[@id="priceblock_ourprice"]/text()').get()
        calificacion = response.xpath('//a[@id="acrCustomerReviewLink"]/span/text()').get()

        # Limpieza de datos
        titulo = titulo.replace('\n', '').replace('\r', '').strip()

        # Guardado de datos en un archivo
        f = open('./excel1b.csv', 'a')
        f.write(titulo + ","+ precio+"," + calificacion )
        f.close()
        
        print('Titulo: '+ titulo)
        print('Precio: '+ precio)
        print('Calificacion: '+calificacion)
        print()

        # No necesito hacer yield. El yield me sirve cuando voy a guardar los datos
        # en un archivo, corriendo Scrapy desde Terminal

# Logica para correr una extraccion de Scrapy periodicamente. Es decir, automatizarla.

print("\n========== Crawler Renta ===========\n")
runner = CrawlerRunner()
task = LoopingCall(lambda: runner.crawl(RentaCrawler)) # Para Investigar: Funciones Anonimas en Python
task.start(2) # Tiempo en segundos desde la primera corrida del programa para repetir la extraccion
reactor.run()
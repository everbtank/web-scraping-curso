from twisted.internet import reactor 
from twisted.internet.task import LoopingCall
from scrapy.crawler import CrawlerRunner
from scrapy.spiders import CrawlSpider, Rule
from scrapy.spiders import Spider
from scrapy.linkextractors import LinkExtractor

# No necesito definir mi abstraccion, porque utilizare otro metodo para guardar datos

class ExtractorRenta(Spider):
    name = "RentaCrawler"
    
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
        'CLOSESPIDER_PAGECOUNT': 20,
        'LOG_ENABLED': True # Elimina los miles de logs que salen al ejecutar Scrapy en terminal
    }
    allowed_domains = ['realtor.com']
    start_urls = ["https://www.realtor.com/rentals","https://www.realtor.com/apartments/New-York_NY","https://www.realtor.com/realestateandhomes-detail/1401-Laurens-View-Rd_Greenville_SC_29607_M68564-69757"]

    download_delay = 1
    
    rules = [Rule(LinkExtractor(allow=r'/realestateandhomes-detail'), follow=True,
                      callback='parse_items')]

    def parse_items(self, response):
        
        #//h1/span[1]/text()
        #
        data_source=response.xpath('//div/text()').get()
        #titulo = response.xpath('//div[@class="ldp-property-meta"]/ul/li[1]/span/text()').get()
        #descripcion = response.xpath('//p[@id="ldp-detail-romance"]/text()').get()
        #price = response.xpath('//*[@id="layout-container"]/div[2]/section[2]/div/div/div[2]/div/div/div[2]/a/div/div[2]/span/').get
        #address = response.xpath('//*[@id="saved_item_6774345402"]/div[2]/div[2]/div[1]/div[1]/a/div[2]/text()[1]').get()
        #city = response.xpath('//*[@id="saved_item_6774345402"]/div[2]/div[2]/div[1]/div[1]/a/div[2]/div/text()').get()
        #state = response.xpath('//*[@id="saved_item_6788806178"]/div[2]/div[2]/div[1]/div[1]/a/div[2]/div/text()[3]').extract()
        #codezip = response.xpath('//*[@id="saved_item_6788806178"]/div[2]/div[2]/div[1]/div[1]/a/div[2]/div/text()[4]').get()
    
        #bad = response.xpath('//*[@id="layout-container"]/div[2]/section[3]/div/div/div[1]/div/div/div[2]/div/div/a/div[1]/div/ul/li[1]/span[1]/b/text()').get()
        #bath = response.xpath('//*[@id="layout-container"]/div[2]/section[3]/div/div/div[1]/div/div/div[2]/div/div/a/div[1]/div/ul/li[2]/span[1]/b/text()').get()
        
        """
        #Limpieza de datos
        titulo = titulo.replace('\n', '').replace('\r', '').strip()
        address = address.replace('°', '').replace('\n', '').replace('\r', '').strip()
        """
        #data_source = data_source.replace('RealFeel®', '').replace('°', '').replace('\n', '').replace('\r', '').strip()
        #titulo = titulo.replace('\n', '').replace('\r', '').strip()
        #descripcion = descripcion.replace('\n', '').replace('\r', '').strip()
        """codezip = price.replace('\n', '').replace('\r', '').strip()
        bad = price.replace('\n', '').replace('\r', '').strip()
        bath = price.replace('\n', '').replace('\r', '').strip()
        """
        
        # Guardado de datos en un archivo
        f = open("./renta.csv", "a")
        # f.write(titulo + "," + address + "," +city+ "," +price+","+state+","+ ","+state+ ","+codezip + "," + bad +"," + bath +",\n")
        f.write(data_source+","+"\n")
        f.close()
        #print(titulo)
        #print(address)"""
        print(data_source)
        #print(titulo)
        #print(descripcion)
        #print(price)
        #print(city)
        #print(state)
        #print(codezip)
        #print(bad)
        #print(bath)
        print()

        # No necesito hacer yield. El yield me sirve cuando voy a guardar los datos
        # en un archivo, corriendo Scrapy desde Terminal

# Logica para correr una extraccion de Scrapy periodicamente. Es decir, automatizarla.
runner = CrawlerRunner()
task = LoopingCall(lambda: runner.crawl(ExtractorRenta)) # Para Investigar: Funciones Anonimas en Python
task.start(20) # Tiempo en segundos desde la primera corrida del programa para repetir la extraccion
reactor.run()


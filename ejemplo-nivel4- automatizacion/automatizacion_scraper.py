from twisted.internet import reactor 
from twisted.internet.task import LoopingCall 
from scrapy.crawler import CrawlerRunner
from scrapy.spiders import Spider

class ExtractorAmazon(Spider):
    name= "MiEXTRACTORAMAZON"
    custom_settings = {
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
        'CLOSESPIDER_PAGECOUNT': 20,
        'LOG_ENABLED': True
    }
    
    start_urls = ["https://www.amazon.es/Lenovo-IdeaPad-Chromebook-Ordenador-Port%C3%A1til/dp/B08WRT63Z2/ref=sr_1_1_sspa?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=laptop&qid=1627523770&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUE0SThCSkxHVlgxNiZlbmNyeXB0ZWRJZD1BMDYwNTEwNzM0MzdSODRWT1pGREMmZW5jcnlwdGVkQWRJZD1BMDE1MjI4OTFTRkFPUDMxR0JUT0omd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl",
                  "https://www.amazon.es/HUAWEI-MatePad-T10s-procesador-cu%C3%A1druples/dp/B08D6N54JB/ref=sr_1_1_sspa?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=tablet&qid=1627522674&s=computers&sr=1-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExMklKSTFDWTQyN1REJmVuY3J5cHRlZElkPUEwMTU5ODQwM0FNNzgxNktXRkhKNCZlbmNyeXB0ZWRBZElkPUEwOTcyNzM0MTEzVElGRVlNTE5TRSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=",
                  "https://www.amazon.es/Smartphone-DotDisplay-Snapdragon-cu%C3%A1druple-auriculares/dp/B08XY935HP/ref=sr_1_1?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=xiaomi&qid=1627523833&sr=8-1"
                  ]
    
    def parse(self,response):
        titulo =response.xpath("//h1[@id='title']/span/text()").get()
        precio =response.xpath("//span[@id='priceblock_ourprice']/text()").get()
        calificacion=response.xpath("//a[@id='acrCustomerReviewLink']/span/text()").get()
        
        titulo = titulo.replace('\n', '').replace('\r', '').strip()
        
        f = open("./datos.csv","a")
        f.write(titulo +","+precio + ","+calificacion +"\n")
        f.close()
        print(titulo)
        print(precio)
        print(calificacion)
        print()
        
        
runner = CrawlerRunner()
task =  LoopingCall(lambda: runner.crawl(ExtractorAmazon))
task.start(20)
reactor.run()

        
        
        
        
    
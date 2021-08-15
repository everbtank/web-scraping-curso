#Automatizar extracion de datos con scrapy 
from twisted.internet import reactor 
from twisted.internet.task import LoopingCall 
from scrapy.crawler import CrawlerRunner
from scrapy.spiders import Spider

class ExtractorAmazon(Spider):
    name = "miextraxtoramazon"
    custom_settings = {
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
        'CLOSESPIDER_PAGECOUNT': 20,
        'LOG_ENABLED': True
    }
    start_urls = ["https://www.amazon.es/HUAWEI-MatePad-10-4-New-Pantalla/dp/B08X77TBT9/ref=sr_1_2_sspa?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1L5I7YWNAP8ID&dchild=1&keywords=tablet&qid=1627524223&sprefix=table%2Caps%2C363&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFTUVgwUVBURklQTU0mZW5jcnlwdGVkSWQ9QTAyOTUyNjUxTDEySjVCVVlTREU1JmVuY3J5cHRlZEFkSWQ9QTA5NzEwNzQzQlpLNTkxRDFUR0kzJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==",
                  "https://www.amazon.es/dp/B0913KRQFR/ref=redir_mobile_desktop?_encoding=UTF8&aaxitk=11a4d9ad159b79b54da0d15122056dcc&hsa_cr_id=6095722140502&pd_rd_plhdr=t&pd_rd_r=4066c53a-f73a-4b7b-8ef7-f8a9c701347c&pd_rd_w=vb3t9&pd_rd_wg=F8G5n&ref_=sbx_be_s_sparkle_mcd_asin_0_img",
                  "https://www.amazon.es/Xiaomi-Redmi-Note-Pro-Smartphone/dp/B08XJXNN9N/ref=sr_1_2?dchild=1&keywords=xiaomi&qid=1627524324&sr=8-2"]
    
    def parse(self,response):
        titulo = response.xpath("//h1[@id='title']/span/text()").get()
        precio = response.xpath("//span[@id='pricebloc_ourprice']/text()").get()
        calificacion = response.xpath("//a[@id='acrCustomerReviewLink']/span/text()").get()
        
        titulo = titulo.replace('\n', '').replace('\r', '').strip()
        
        f= open("./datos.csv","a")
        f.write(titulo+","+ precio + ","+calificacion+"\n")
        f.close()
        print(titulo)
        print(precio)
        print(calificacion)
        print()
        
runner = CrawlerRunner()
task = LoopingCall(lambda: runner.crawl(ExtractorAmazon))
task.start(20)
reactor.run()    
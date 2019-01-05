import scrapy
from mercadolivre.items import MercadolivreItem


class QuotesSpider(scrapy.Spider):
    name = "mercado-produto"

    def start_requests(self):
        urls = [
            'https://esportes.mercadolivre.com.br/suplementos/#menu=categories',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        links_produtos = list(set(response.xpath('//ol[@id="searchResults"]//a/@href').extract()))
        for url in links_produtos:
            yield scrapy.Request(url=url, callback=self.parse_produto)
        
        next_page_url = response.xpath('//li/a[@class="andes-pagination__link prefetch"]/@href').extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
    
    def parse_produto(self,response):
        produto = MercadolivreItem()
        produto['nome'] = response.xpath('//h1[@class="item-title__primary "]/text()').extract_first().strip()
        produto['preco'] = response.xpath('//span[@class="price-tag-symbol"]/@content').extract_first()
        produto['img_link'] = response.xpath('//div[@id="gallery_dflt"]//a/@href').extract()
        produto['loja_nome'] = response.xpath('//div[@class="official-store-container "]//p[@class="title"]/text()').extract_first()
        yield produto

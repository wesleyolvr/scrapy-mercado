# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MercadolivreItem(scrapy.Item):
    Nome = scrapy.Field()
    Preco = scrapy.Field()
    loja_nome = scrapy.Field()
    img_link = scrapy.Field()
    url_produto = scrapy.Field()


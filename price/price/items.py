# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PriceItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    collection = 'prices'

    date = scrapy.Field()
    product = scrapy.Field()
    price = scrapy.Field()
    market = scrapy.Field()
    pass


# class MarketItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     collection = 'market'

#     #name = scrapy.Field()
#     #address = scrapy.Field()
#     href = scrapy.Field()
    

    

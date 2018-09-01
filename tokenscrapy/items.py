# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TokenscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()
    image_url = scrapy.Field()
    name = scrapy.Field()
    example = scrapy.Field()
    des = scrapy.Field()
    price = scrapy.Field()
    change = scrapy.Field()
    volume = scrapy.Field()
    market_cap = scrapy.Field()



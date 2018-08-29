# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class VipspdierItem(scrapy.Item):
    # 商品介绍
    info = scrapy.Field()
    # 原价
    orin_price = scrapy.Field()
    # 现价
    price = scrapy.Field()
    # 折扣
    discount = scrapy.Field()
    # 二级页面url
    next_url = scrapy.Field()

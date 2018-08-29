# -*- coding: utf-8 -*-
import scrapy
from VipSpdier.items import VipspdierItem

class VipSpider(scrapy.Spider):
    name = 'vip'
    allowed_domains = ['vip.com']
    start_urls = ['http://category.vip.com/suggest.php?keyword=%E8%BF%9E%E8%A1%A3%E8%A3%99']



    def parse(self, response):
        goods_list = response.xpath("//div[starts-with(@id,'J_pro_')]")
        print(goods_list)
        for goods in goods_list:
            item = VipspdierItem()
            item["info"] = goods.xpath(".//a[@rel='noopener']/text()").extract_first()
            # 其他，自己写

            # 详情页url
            next_url = "http:" +goods.xpath(".//a[@rel='noopener']/@href").extract_first()
            yield scrapy.Request(url=next_url,callback=self.parse_next)

    def parse_next(self,response):
        print(response)
        pass
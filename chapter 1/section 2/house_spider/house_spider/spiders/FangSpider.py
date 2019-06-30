# -*- coding: utf-8 -*-
import scrapy
from house_spider.items import HouseItem


class FangspiderSpider(scrapy.Spider):
    name = 'FangSpider'
    allowed_domains = ['fang.com']

    def start_requests(self):
        yield scrapy.Request('https://esf.fang.com/',
                             callback=self.parse,
                             headers={
                                 'referer': 'https://www.fang.com',
                             },
                             dont_filter=True)

    def parse(self, response):
        lists = response.css('div.shop_list > dl  dd > h4 > a')

        for info in lists:
            # 直接把a标签的css选择器传入
            yield response.follow(info,
                                  callback=self.parse_info,
                                  dont_filter=True)

    def parse_info(self, response):
        item = HouseItem()
        item['title'] = response.css('h1.title::text').get().strip()
        item['total_price'] = response.css(
            'div.price_esf i::text').get().strip()
        item['area'] = response.css(
            'div.tab-cont.clearfix > div.tab-cont-right > div:nth-child(2) > div.trl-item1.w182 > div.tt::text'
        ).get()
        item['direction'] = response.css(
            'div.tab-cont.clearfix > div.tab-cont-right > div:nth-child(3) > div.trl-item1.w146 > div.tt::text'
        ).get().strip()
        item['community'] = response.css(
            'div.tab-cont.clearfix > div.tab-cont-right > div:nth-child(4) > div:nth-child(1) > div.rcont a::text'
        ).get()
        yield item

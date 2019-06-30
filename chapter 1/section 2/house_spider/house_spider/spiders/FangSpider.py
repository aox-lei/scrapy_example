# -*- coding: utf-8 -*-
import scrapy
from house_spider.items import FangSpiderEsfListItem


class FangspiderSpider(scrapy.Spider):
    name = 'FangSpider'
    allowed_domains = ['fang.com']

    def start_requests(self):
        yield scrapy.Request('https://esf.fang.com/')

    def parse(self, response):
        lists = response.css('div.shop_list > dl')

        for info in lists:
            item = FangSpiderEsfListItem()
            item['title'] = info.css('dd > h4 > a > span::text').get()
            item['total_price'] = info.css(
                'dd.price_right > span.red > b::text').get()
            item['url'] = info.css('dd > h4 > a::attr("href")').get()
            yield item

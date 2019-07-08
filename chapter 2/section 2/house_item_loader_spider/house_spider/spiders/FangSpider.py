# -*- coding: utf-8 -*-
import scrapy
from house_spider.items import HouseItem, HouseItemLoader


class FangSpider(scrapy.Spider):
    name = 'FangSpider'
    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {
            'referer': 'https://www.fang.com',
        }
    }

    def start_requests(self):
        yield scrapy.Request(
            'https://esf.fang.com/chushou/3_435332626.htm?channel=2,2&psid=1_1_40/',
            callback=self.parse,
            dont_filter=True)

    def parse(self, response):
        item = HouseItemLoader(HouseItem(), response)
        item.add_css('title', '#lpname > h1::text')
        item.add_value('title', '这是附标题')
        print(item.load_item())

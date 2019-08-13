# -*- coding: utf-8 -*-
import scrapy
from ccidcom.items import DocumentItem


class CcidcomSpider(scrapy.Spider):
    name = 'ccidcomSpider'
    allowed_domains = ['www.ccidcom.com']
    start_urls = ['http://www.ccidcom.com/yaowen/index.html']

    def start_urls(self):
        yield scrapy.Request('http://www.ccidcom.com/yaowen/index.html', callback=self.parse)

    def parse(self, response):
        pass

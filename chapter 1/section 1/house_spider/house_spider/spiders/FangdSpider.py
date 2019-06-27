# -*- coding: utf-8 -*-
import scrapy


class FangdspiderSpider(scrapy.Spider):
    name = 'FangdSpider'
    allowed_domains = ['fang.com']
    start_urls = ['http://fang.com/']

    def parse(self, response):
        pass

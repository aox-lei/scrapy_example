# -*- coding: utf-8 -*-
import scrapy
from house_spider.items import HouseItem
from scrapy.linkextractors import LinkExtractor


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
        links = LinkExtractor(allow=('\/chushou\/(.*)\.htm', ))
        links = links.extract_links(response)
        for info in links:
            yield scrapy.Request(info.url,
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


import scrapy
from scrapy.spiders import CrawlSpider, Rule
from house_spider.items import HouseItem
from scrapy.linkextractors import LinkExtractor


class FangSpider(CrawlSpider):
    name = 'FangCrawlSpider'
    allowed_domains = ['fang.com']
    start_urls = ['https://esf.fang.com']
    rules = (Rule(LinkExtractor(allow=('chushou\/(.*)\.htm', )),
                  callback='parse_info'), )
    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {
            'referer': 'https://www.fang.com',
        }
    }

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
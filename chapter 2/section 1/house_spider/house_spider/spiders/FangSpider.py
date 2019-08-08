# -*- coding: utf-8 -*-
import scrapy
from house_spider.items import HouseItem


class FangSpider(scrapy.Spider):
    '''
    测试Telnet Console
    '''
    name = 'FangSpider'
    allowed_domains = ['fang.com']

    # 房天下有反爬机制, 会通过cookie验证, 所以添加这一段来破解反爬, 如果失效则重新copy一个cookie出来即可
    # 后面会有教程讲如何自动破解

    def start_requests(self):
        yield scrapy.Request(url='https://esf.fang.com',
                             cookies={
                                 'city':
                                 'www',
                                 'global_cookie':
                                 'tixt3tpiedn0brb7m4t9pl9fd2zjyb8wtwc',
                                 'unique_cookie':
                                 'U_tixt3tpiedn0brb7m4t9pl9fd2zjyb8wtwc'
                             },
                             dont_filter=True,
                             meta={'cookiejar': 1})

    def parse(self, response):
        for i in range(1, 10):
            yield scrapy.Request('https://esf.fang.com/',
                                 callback=self.parse,
                                 dont_filter=True)


class FangItemSpider(scrapy.Spider):
    '''
    测试scrapy parse
    '''
    name = 'FangItemSpider'
    allowed_domains = ['fang.com']

    def start_requests(self):
        yield scrapy.Request(url='https://esf.fang.com',
                             cookies={
                                 'city':
                                 'www',
                                 'global_cookie':
                                 'tixt3tpiedn0brb7m4t9pl9fd2zjyb8wtwc',
                                 'unique_cookie':
                                 'U_tixt3tpiedn0brb7m4t9pl9fd2zjyb8wtwc'
                             },
                             dont_filter=True,
                             meta={'cookiejar': 1})

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


from scrapy.shell import inspect_response


class FangShellSpider(scrapy.Spider):
    '''
    测试scrapy断点shell调试
    '''
    name = 'FangShellSpider'
    allowed_domains = ['fang.com']
    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {
            'referer': 'https://www.fang.com',
        }
    }

    def start_requests(self):
        yield scrapy.Request('https://esf.fang.com/',
                             callback=self.parse,
                             dont_filter=True)

    def parse(self, response):
        inspect_response(response=response, spider=self)
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
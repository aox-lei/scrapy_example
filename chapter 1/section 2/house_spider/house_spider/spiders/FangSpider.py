# -*- coding: utf-8 -*-
import scrapy
from house_spider.items import HouseItem


class FangspiderSpider(scrapy.Spider):
    name = 'FangSpider'
    allowed_domains = ['fang.com']
    # 房天下有反爬机制, 会通过cookie验证, 所以添加这一段来破解反爬, 如果失效则重新copy一个cookie出来即可
    # 后面会有教程讲如何自动破解
    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {
            'Referer':
            'https://esf.fang.com',
            'Cookie':
            'global_cookie=ts9lekodlmqrdd8ikgqjno2r91zjy08to2g; budgetLayer=1%7Cbj%7C2019-07-12%2023%3A15%3A42; lastscanpage=0; resourceDetail=1; city=www; Integrateactivity=notincludemc; logGuid=1d7ea639-c548-4b51-b36b-5f33d15bb8fc; __utma=147393320.1729056910.1562944544.1562944544.1563609816.2; __utmc=147393320; __utmz=147393320.1563609816.2.2.utmcsr=search.fang.com|utmccn=(referral)|utmcmd=referral|utmcct=/captcha-verify/redirect; __utmt_t0=1; __utmt_t1=1; __utmt_t2=1; g_sourcepage=undefined; unique_cookie=U_tixt3tpiedn0brb7m4t9pl9fd2zjyb8wtwc*4; __utmb=147393320.12.10.1563609816'
        }
    }

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

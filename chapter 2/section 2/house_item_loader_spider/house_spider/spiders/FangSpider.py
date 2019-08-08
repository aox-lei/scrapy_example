# -*- coding: utf-8 -*-
import scrapy
from house_spider.items import HouseItem, HouseItemLoader


class FangSpider(scrapy.Spider):
    name = 'FangSpider'

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
        item = HouseItemLoader(HouseItem(), response)
        item.add_css('title', '#lpname > h1::text')
        item.add_value('title', '这是附标题')
        print(item.load_item())

# -*- coding: utf-8 -*-
import scrapy
from ccidcom.items import DocumentItem


class CcidcomSpider(scrapy.Spider):
    name = 'ccidcomSpider'
    allowed_domains = ['www.ccidcom.com']

    def start_requests(self):
        yield scrapy.Request(
            'http://www.ccidcom.com/yaowen/index.html',
            callback=self.parse,
            headers={  # 指定请求头
                'Content-Type': 'text',
            },
            cookies={'test_cookie': 'aaa'},
            meta={
                'column': 'yaowen',
                'bindaddress': ('114.114.114.114', 0)
            },
            dont_filter=True,
            errback=self.parse_error,
            cb_kwargs={'column': 'yaowen'})

    def parse(self, response, column):
        print(response.text)
        request = response.request
        print('自定义参数: ', column)
        print('请求头: ', request.headers)
        print('请求Cookies: ', request.cookies)
        print('元数据: ', response.meta)

    def parse_error(self, response):
        pass
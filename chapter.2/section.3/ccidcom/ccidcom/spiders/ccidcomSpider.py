# -*- coding: utf-8 -*-
import scrapy

from ccidcom.items import DocumentItem


class CcidcomSpider(scrapy.Spider):
    name = 'ccidcomSpider'
    allowed_domains = ['www.ccidcom.com']

    def start_requests(self):
        yield scrapy.Request('http://www.ccidcom.com/yaowen/index.html',
                             callback=self.parse,
                             dont_filter=True,
                             flags=['yaowen'])

    def parse(self, response):
        print('请求的url: ', response.url)
        print('http code: ', response.status)
        print('headers: ', response.headers)
        print('headers Set-Cookie: ', response.headers.get('Set-Cookie'))
        print('headers Set-Cookie list: ', response.headers.getlist('Set-Cookie'))
        print('body的type类型:', type(response.body))
        print('flags: ', response.flags)
        print('request.flags: ', response.request.flags)
        print('request: ', response.request)

    def parse_error(self, response):
        pass

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
        print('headers Set-Cookie list: ',
              response.headers.getlist('Set-Cookie'))
        print('body的type类型:', type(response.body))
        print('flags: ', response.flags)
        print('request.flags: ', response.request.flags)
        print('request: ', response.request)

    def parse_error(self, response):
        pass


class ResponseSpider(scrapy.Spider):
    name = 'ResponseSpider'

    def start_requests(self):
        yield scrapy.Request('http://www.ccidcom.com/yaowen/index.html',
                             callback=self.parse,
                             dont_filter=True)

    def parse(self, response):
        new_response = response.copy()
        print('新对象内存地址:', id(new_response))
        print('旧对象内存地址:', id(response))
        # 使用replace 替换请求的url
        new_response = response.replace(url='http://www.baidu.com')
        print('旧对象请求的url:', response.url)
        print('新对象请求的url:', new_response.url)
        # 拼接url, 输出: http://www.ccidcom.com/baidu
        print(response.urljoin('/baidu'))

        article_list_selector = response.css('div.artlisting div.article-item')
        for article_selector in article_list_selector:
            yield response.follow(article_selector.css('div.title a')[0], callback=self.parse_article)

    def parse_article(self, response):
        print(response.css('title::text').get())

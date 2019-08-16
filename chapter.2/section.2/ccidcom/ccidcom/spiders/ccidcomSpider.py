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


class CcidcomFormSpider(scrapy.Spider):
    name = 'CcidcomFormSpider'

    def start_requests(self):
        yield scrapy.FormRequest(url='http://www.ccidcom.com/user/dologin.do',
                                 formdata={
                                     'username': '你的账号',
                                     'password': '你的登录密码'
                                 },
                                 callback=self.after_login)

    def after_login(self, response):
        print('返回的数据: {}'.format(response.text))


class CcidcomFromResponseSpider(scrapy.Spider):
    name = 'CcidcomFromResponseSpider'

    def start_requests(self):
        # 先访问表单所在的页面
        yield scrapy.Request('http://www.dcic-china.com/login/index.html',
                             callback=self.parse)

    def parse(self, response):
        # 这个方法会将上一个表单页面的资源传入, 并且自动解析表单元素
        # 然后补足你提供的表单的值(你自定义的值可能会覆盖表单页面的值)
        yield scrapy.FormRequest.from_response(response,
                                               formdata={
                                                   'username': '你的账号',
                                                   'password': '你的密码',
                                                   'code': '1111'
                                               },
                                               callback=self.after_login)

    def after_login(self, response):
        print('返回的数据: {}'.format(response.css('p.error::text').get()))
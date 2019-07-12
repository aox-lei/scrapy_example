# -*- coding: utf-8 -*-
import scrapy
from house_spider.items import HouseItem, HouseItemLoader, CommunityItem, CommunityItemLoader
from scrapy.http.cookies import CookieJar

cookie_jar = CookieJar()


class CcidnetCookieSpider(scrapy.Spider):
    '''
    模拟登录
    '''
    name = 'CcidnetCookieSpider'

    def start_requests(self):
        yield scrapy.Request(
            'http://app.ccidnet.com/?app=member&controller=index&action=login',
            callback=self.login,
            dont_filter=True
            meta={'cookiejar': 1}
        )

    def login(self, response):
        yield scrapy.FormRequest(
            'http://app.ccidnet.com/?app=member&controller=index&action=login',
            formdata={
                'username': '123123',
                'password': '123123',
                'seccode': '123456',
                'login-button': '登录',
                'show_qr': '0'
            },
            # 继续传递cookiejar
            meta={'cookiejar': response.meta['cookiejar']},
            callback=self.after_login)

    def after_login(self, response):
        # 解析cookie
        cookies = cookie_jar.extract_cookies(response, response.request)
        result = response.css('div.content > h1::text').get()
        # 在之后的yield中都需要带有meta
        # yield scrapy.Request(meta={'cookiejar': response.meta['cookiejar']})
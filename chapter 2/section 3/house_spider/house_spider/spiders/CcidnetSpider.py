# -*- coding: utf-8 -*-
import scrapy
from house_spider.items import HouseItem, HouseItemLoader, CommunityItem, CommunityItemLoader


class CcidnetSpider(scrapy.Spider):
    '''
    模拟登录
    '''
    name = 'CcidnetSpider'

    def start_requests(self):
        yield scrapy.Request(
            'http://app.ccidnet.com/?app=member&controller=index&action=login',
            callback=self.login,
            dont_filter=True)

    def login(self, response):
        yield scrapy.FormRequest.from_response(response,
                                               formdata={
                                                   'username': '123123',
                                                   'password': '123123',
                                                   'code': '12345'
                                               },
                                               callback=self.after_login)

    def after_login(self, response):
        result = response.css('div.content > h1::text').get()
        print('模拟登录结果: ' + result)

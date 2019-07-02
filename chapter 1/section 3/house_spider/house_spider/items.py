# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HouseSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class FangSpiderEsfListItem(scrapy.Item):
    '''
    房天下二手房列表页Item
    '''
    title = scrapy.Field()  # 标题
    total_price = scrapy.Field()  # 总价
    url = scrapy.Field()  # 详情页url


class HouseItem(scrapy.Item):
    '''
    房源信息
    '''
    title = scrapy.Field()  # 标题
    total_price = scrapy.Field()  # 总价
    area = scrapy.Field()  # 面积
    direction = scrapy.Field()  # 朝向
    community = scrapy.Field()  # 小区
    url = scrapy.Field()  # 详情页url

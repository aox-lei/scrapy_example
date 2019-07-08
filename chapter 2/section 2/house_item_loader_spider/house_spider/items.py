# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join, Compose


def remove_blank(value):
    return value.strip()


class HouseItemLoader(ItemLoader):
    title_in = Compose(TakeFirst(), remove_blank)
    title_out = Join('-----')


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

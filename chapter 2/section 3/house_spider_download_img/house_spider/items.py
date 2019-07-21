# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join, Compose, Identity


def remove_blank(value):
    return value.strip()


class DefaultItemLoader(ItemLoader):
    default_input_processor = Compose(TakeFirst(), remove_blank)
    default_output_processor = TakeFirst()


class HouseItemLoader(DefaultItemLoader):
    image_urls_out = Identity()


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
    image_urls = scrapy.Field()
    image_paths = scrapy.Field()
    images = scrapy.Field()


class CommunityItemLoader(DefaultItemLoader):
    pass


class CommunityItem(scrapy.Item):
    '''
    小区信息
    '''
    name = scrapy.Field()  # 小区名称
    address = scrapy.Field()  # 小区地址
    area = scrapy.Field()  # 小区所属区域

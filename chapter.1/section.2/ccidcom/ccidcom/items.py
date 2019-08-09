# -*- coding: utf-8 -*-
import scrapy


class CcidcomItem(scrapy.Item):

    pass


class DocumentItem(scrapy.Item):
    title = scrapy.Field()
    writer = scrapy.Field()
    publish_time = scrapy.Field()
    source = scrapy.Field()
    content = scrapy.Field()
    url = scrapy.Field()
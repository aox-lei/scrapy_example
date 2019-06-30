# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from house_spider.mongo import House


class HouseSpiderPipeline(object):
    def process_item(self, item, spider):
        try:
            house_mongo = House(**item)
            house_mongo.save()
            return item
        except Exception as e:
            print('保存数据失败', item)
            return False

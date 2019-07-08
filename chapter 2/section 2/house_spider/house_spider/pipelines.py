# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from house_spider.mongo import House, Community
from house_spider.items import HouseItem, CommunityItem
from scrapy.exceptions import DropItem

class HouseSpiderPipeline(object):
    def process_item(self, item, spider):
        if type(item) != HouseItem:
            return item

        if int(item.get('total_price')) > 100:
            raise DropItem('价格太高了! 不要！！！')
        
        try:
            house_mongo = House(**item)
            house_mongo.save()
            return item
        except Exception as e:
            print('保存数据失败', item)
            return False


class CommunityPipeline(object):
    def process_item(self, item, spider):
        if type(item) != CommunityItem:
            return item

        try:
            community_mongo = Community(**item)
            community_mongo.save()
            return item
        except Exception as e:
            print('保存数据失败', item)
            return False
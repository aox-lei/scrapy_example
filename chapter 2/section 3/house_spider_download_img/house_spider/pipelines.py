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


from scrapy.pipelines.images import ImagesPipeline
import scrapy


class ImagesPipeline(object):
    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item
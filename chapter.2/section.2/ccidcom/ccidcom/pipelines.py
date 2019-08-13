# -*- coding: utf-8 -*-
import json


class CcidcomPipeline(object):
    def process_item(self, item, spider):
        """处理爬虫传过来的数据

        将item进行json处理后, 保存到指定的文件中
        
        Arguments:
            item {dict} -- 数据的item对象
            spider {object} -- 产生item数据的爬虫
        
        Returns:
            dict -- Item对象
        """
        path = './documents'
        file_path = '{}/{}.json'.format(path, item['title'])
        with open(file_path, 'w') as f:
            f.write(json.dumps(dict(item)))
        return item

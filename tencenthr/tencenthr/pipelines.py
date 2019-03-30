# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient

client = MongoClient(host="192.168.1.107", port=27017)
collection = client["tencent"]["hr1"]


class TencenthrPipeline(object):
    def process_item(self, item, spider):
        collection.insert(dict(item))
        print(item)
        return item

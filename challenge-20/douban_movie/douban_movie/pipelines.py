# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import redis
import re
import json
from scrapy.exceptions import DropItem

class DoubanMoviePipeline(object):
    count = 0
    def open_spider(self,spider):
        self.r = redis.StrictRedis(host='127.0.0.1',port=6379,decode_responses=True)


    def process_item(self, item, spider):
        if eval(item['score']) < 8:
            raise DropItem
        DoubanMoviePipeline.count+=1
        self.r.lpush('douban_movie:items',json.dumps(dict(item)))
        return item



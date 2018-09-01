# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import logging
import pymongo



class TokenscrapyPipeline(object):

    # filename = 'tokensspider.txt'
    # def open_spider(self, spider):
    #     self.file = open(self.filename, 'w')
    #
    # def close_spider(self, spider):
    #     self.file.close()
    #
    # def process_item(self, item, spider):
    #     try:
    #         line = json.dumps(dict(item)) + "\n"
    #         logging.info(line)
    #         self.file.write(line)
    #     except:
    #         pass

    collection_name = 'scrapy'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGODB_DB')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        # ids = self.db[self.collection_name].insert_one(dict(item))
        item_dic = dict(item)
        ids = self.db[self.collection_name].update(
            {'id': item_dic['id']},
            item_dic,
            upsert=True
        )
        logging.info("process_item:" + str(ids))
        return item


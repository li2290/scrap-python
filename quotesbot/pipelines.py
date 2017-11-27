# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os
import json
import MySQLdb
import scrapy
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem
from settings import IMAGES_STORE as image_store
class QuotesbotPipeline(object):
	def __init__(self):
		self.db = MySQLdb.connect("localhost","lzq","WhCyILfkssvYbfNh","yiitest",use_unicode=True, charset="utf8" )
		print "open***************************************************************************************"
		self.f=open("aa.json","w")
		#pass
	def process_item(self, item, spider):
		print "donging***************************************************************************************"
		content=json.dumps(dict(item),ensure_ascii=False)+",\n"
		self.f.write(content)
		cursor = self.db.cursor()
		if spider.name=="img":
			cursor.execute('INSERT INTO `lzq_py`( `imagelink`, `nickname`) VALUES (%s,%s)', (item['nickname'],item['imagelink']))
		else:
			cursor.execute('INSERT INTO `lzq_py`( `imagelink`, `nickname`) VALUES (%s,%s)', ("liao","zq"))
		#print "doing212313213123123123123123123123123123************************************************************"
		self.db.commit()
		return item
	def close_spider(self , spider):
		self.f.close()
		self.db.close()
		print "closeing***************************************************************************************"
class douyuPipeline(ImagesPipeline):
	def get_media_requests(self, item, info):
		print "doing2************************************************************"
		item=dict(item)
		if item.has_key("imagelink"):
			if len(item['imagelink'])>0:
				image_url = item['imagelink']
				yield scrapy.Request(image_url)

	def item_completed(self, results, item, info):
		print "doing3************************************************************"
		item=dict(item)
		if item.has_key("imagelink"):
			if len(item['imagelink'])>0:
				image_paths = [x['path'] for ok, x in results if ok]
				os.rename(image_store+image_paths[0],image_store+item["nickname"]+".jpg")
				#yield item  这里千万别加这个东西要不然会返回<generator object item_completed at 0x000000000614EF78>

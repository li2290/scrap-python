# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QuotesbotItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	text=scrapy.Field()
	author=scrapy.Field()
	tags=scrapy.Field()
    #pass

class LiaoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    nickname=scrapy.Field()
    imagelink=scrapy.Field()
class TianItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    nickname=scrapy.Field()
    color=scrapy.Field()
    size=scrapy.Field()
    ratecontent=scrapy.Field()
    ratedate=scrapy.Field()

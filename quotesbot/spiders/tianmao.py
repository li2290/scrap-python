import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import scrapy
import json
import re
from quotesbot.items import TianItem

class TianmaioSpider(scrapy.Spider):
	name = 'tianmao'
	#allowed_domains = ['http://www.itcast.cn']
	#start_urls = ['http://www.itcast.cn/channel/teacher.shtml']
	#start_urls = ['http://hr.tencent.com/position.php?&start=0']
	baseurl="https://rate.tmall.com/list_detail_rate.htm?itemId=546402041845&spuId=724285208&sellerId=1800399917&order=3&currentPage="
	offset=0
	#start_urls=[baseurl+str(offset)]
	
	def start_requests(self):
		return [scrapy.FormRequest(self.baseurl+str(self.offset),
			cookies={"cna":"ealLEiM6RRwCATuuOZ0exkYh"," tk_trace":"1"," hng":"CN%7Czh-CN%7CCNY%7C156"," t":"34e27f1bc97c512a43bf0990b3936ae3"," _tb_token_":"33e8ee73b03a9"," cookie2":"13128dca32cc1c7bb91fcd89eb08498b"," JSESSIONID":"75712A331B599DCCAE64F8A3FF017654", "isg":"AoaGbRFyIIp7YPc9DOQ3t_Th13zIT8sMrf5EUnCrY6k_cy6N2HVksHVBPZlE"},
			callback=self.parse)]
	
	def parse(self, response):
		#print response.body
		content=response.body

		nickname=re.findall(r'"displayUserNick":"(.*?)"',content)
		color=re.findall(r'"cmsSource":"(.*?)"',content)
		size=re.findall(r'"auctionSku":"(.*?)"',content)
		ratecontent=re.findall(r'"rateContent":"(.*?)"',content)
		ratedate=re.findall(r'"rateDate":"(.*?)"',content)
		if len(nickname)==0:
			return
		for i in list(range(0,len(nickname))):
			item=TianItem()
			item['nickname']=nickname[i]
			item['color']=color[i]
			item['size']=size[i]
			item['ratedate']=ratedate[i]
			item['ratecontent']=ratecontent[i]
			yield item
		self.offset+=1
		url=self.baseurl+str(self.offset)
		yield scrapy.Request(url,cookies={"cna":"ealLEiM6RRwCATuuOZ0exkYh"," tk_trace":"1"," hng":"CN%7Czh-CN%7CCNY%7C156"," t":"34e27f1bc97c512a43bf0990b3936ae3"," _tb_token_":"33e8ee73b03a9"," cookie2":"13128dca32cc1c7bb91fcd89eb08498b"," JSESSIONID":"75712A331B599DCCAE64F8A3FF017654", "isg":"AoaGbRFyIIp7YPc9DOQ3t_Th13zIT8sMrf5EUnCrY6k_cy6N2HVksHVBPZlE"},callback=self.parse)
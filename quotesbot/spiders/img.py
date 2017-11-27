import scrapy
import json
from quotesbot.items import LiaoItem

class TestSpider(scrapy.Spider):
	name = 'img'
	#allowed_domains = ['http://www.itcast.cn']
	#start_urls = ['http://www.itcast.cn/channel/teacher.shtml']
	#start_urls = ['http://hr.tencent.com/position.php?&start=0']
	baseurl="http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=2&offset="
	offset=0
	start_urls=[baseurl+str(offset)]
	def parse(self, response):
		data_list=json.loads(response.body)['data']
		if len(data_list)==0:
			return
		for data in data_list:
			item=LiaoItem()
			item['nickname']=data['nickname']
			item['imagelink']=data['vertical_src']
			yield item
		self.offset+=10
		url=self.baseurl+str(self.offset)
		#yield scrapy.Request(url,callback=self.parse)
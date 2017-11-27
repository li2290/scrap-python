# -*- coding: utf-8 -*-
import scrapy
from quotesbot.items import QuotesbotItem

class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'toscrape-xpath'
    start_urls = [
        'http://quotes.toscrape.com/',
		#"https://rate.tmall.com/list_detail_rate.htm?itemId=557518415843&spuId=870527097&sellerId=2024314280&order=3&currentPage=1",
    ]

    def parse(self, response):
	
	
	

        for quote in response.xpath('//div[@class="quote"]'):
			item=QuotesbotItem()
          
			item['text']=quote.xpath('.//span[@class="text"]/text()').extract_first()
			item['author']=quote.xpath('.//small[@class="author"]/text()').extract_first()
			item['tags']=quote.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').extract()
			
			yield item
			
        next_page_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
	
		

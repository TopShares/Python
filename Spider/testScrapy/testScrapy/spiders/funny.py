# -*- coding: utf-8 -*-
import scrapy
import os
from ..items import TestscrapyItem
# from scrapy.http.response.html import HtmlResponse
import re
class FunnySpider(scrapy.Spider):
    name = 'funny'
    allowed_domains = ['784hd.com']
    start_urls = ['http://784hd.com/forum-98-1.html'] # 50
    base_domain = 'http://www.784hd.com/'


    def parse(self, response):
        threadlist = response.xpath('//*[@id="threadlist"]/div//tr/th/a[2]')
        for td in threadlist:
            text = td.xpath('.//text()').get().strip()
            # rep = re.compile(r'.*?[丝].*?')  # 足ストッキング
            # new = re.findall(rep, text)
            # if new:
            url = td.xpath('.//@href').get().strip()
            yield scrapy.Request(url=self.base_domain+url,callback=self.parese_info,meta={"info":(text)},dont_filter=True)

        next_url = response.xpath('//a[@class="nxt"]/@href').get()
        if next_url:
            yield scrapy.Request(url=response.urljoin(next_url),callback=self.parse)

    def parese_info(self, response):

        name = response.meta.get('info')
        urls = response.xpath('//td[@class="t_f"]/img/@file').getall()
        item = TestscrapyItem(image_urls=urls,name=name)
        yield item
        # for img in tbody:
        #     url = img.xpath('./img/@file').getall()
        #     # url = i.xpath('.//@src').get().strip()
        #     print(url)
        #     print("82378737377377")
        # urls = list(map(lambda url:response.urljoin(url), urls))
        # print(urls)
        #     author = i.xpath('.//h2/text()').get().strip()
        #     content = i.xpath('.//div[@class="content"]//text()').getall()
        #     content = ''.join(content).strip()
        #     item = TestscrapyItem(author=author, content=content)
        #     yield item
        #
        # next_url = response.xpath("//ul[@class='pagination']/li[last()]/a/@href").get()
        # print(next_url)
        # if not next_url:
        #     return
        # else:
        #     yield scrapy.Request(self.base_domain+next_url, callback=self.parse,  dont_filter=True)

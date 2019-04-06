# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from urllib import request
from scrapy.pipelines.images import ImagesPipeline
from ..testScrapy import settings
# class TestscrapyPipeline(object):
    # def __init__(self):
    #     self.fp = open("data.json","w", encoding='utf-8')
    #
    # def open_spider(self, spider):
    #     print('spider start ...')
    #
    # def process_item(self, item, spider):
    #     item_json  = json.dumps(dict(item), ensure_ascii=False)
    #     self.fp.write(item_json+'\n')
    #     return item
    #
    # def close_spider(self, spider):
    #     print('spider end')

class TestscrapyPipeline(object):
    def __init__(self):
        self.path = os.path.abspath('images')
        if not os.path.exists(self.path):
            os.makedirs(self.path)
            print(self.path)

    def open_spider(self, spider):
        print('spider start ...')

    def process_item(self, item, spider):
        name = item['name']
        urls = item['urls']
        for url in urls:
            request.urlretrieve(url, self.path)
        return item

    def close_spider(self, spider):
        print('spider end')



class ImgPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        request_objs = super(ImgPipeline, self).get_media_requests(item,info)
        for request_obj in request_objs:
            request_obj.item = item
        return request_objs


    def file_path(self, request, response=None, info=None):
        path = super(ImgPipeline, self).file_path(request, response,info)
        name = request.item.get('name')
        images_store = settings.IMAGES_STORE
        # image_name = path.replace('full/','')
        image_name = name + path.replace('full/','')
        image_path = os.path.join(images_store, image_name)
        return image_path







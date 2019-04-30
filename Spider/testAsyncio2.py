import time
import aiohttp
import asyncio
# from scrapy import Selector

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
}


# 获取网页（文本信息）
async def fetch(session, url):
    async with session.get(url, headers=headers) as response:
        return await response.text(encoding='utf-8')

# 获取每一页的所有图片路径
async def url_parse(html):
    selector = Selector(text=html)
    url_list = selector.xpath('//ul[@class="ali"]//li//img/@src').extract()
    return url_list

# 进行图片的下载
async def down_img(session, url_list):
    for each_url in img_list:
        print('程序正在采集%s' % each_url)
        async with session.get(each_url, headers=headers) as response:
            img_response = await response.read()
            with open('./image/%s.jpg' % time.time(), 'wb') as file:
                file.write(img_response)


# 开始执行抓取
async def start(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url)  # 得到每一页的html
        url_list = await url_parse(html)  # 解析得到每一页的图片url
        await down_img(session, url_list) # 进行图片的下载


if __name__ == '__main__':
    each_url = "http://www.ivsky.com/tupian/ziranfengguang/index_{page}.html"
    full_urllist = [each_url.format(page=i) for i in range(1, 20)]
    event_loop = asyncio.get_event_loop()
    tasks = [start(url) for url in full_urllist]
    tasks = asyncio.wait(tasks)
    event_loop.run_until_complete(tasks)  # 等待任务结束
# encoding:utf-8
import re
import os
import json
import time
import aiohttp
import asyncio
from lxml import etree

class Crawler:

    def __init__(self, urls, max_workers=8):
        self.urls = urls
        self.folder = ''
        self.fetching = asyncio.Queue()
        self.max_workers = max_workers
        self.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
        'Referer': 'https://www.sandpay.com.cn/shop/merchantList.html',
        'Host': 'www.sandpay.com.cn',
    }
    async def crawl(self):
        # DON'T await here; start consuming things out of the queue, and
        # meanwhile execution of this function continues. We'll start two
        # coroutines for fetching and two coroutines for processing.
        all_the_coros = asyncio.gather(
            *[self._worker(i) for i in range(self.max_workers)])

        # place all URLs on the queue
        for url in self.urls:
            await self.fetching.put(url)

        # now put a bunch of `None`'s in the queue as signals to the workers
        # that there are no more items in the queue.
        for _ in range(self.max_workers):
            await self.fetching.put(None)

        # now make sure everything is done
        await all_the_coros

    async def _worker(self, i):
        while True:
            url = await self.fetching.get()
            if url is None:
                # this coroutine is done; simply return to exit
                return

            # print(f'Fetch worker {i} is fetching a URL: {url}')
            async with aiohttp.ClientSession() as session:
                await self.SaveData(session, url)

    async def SaveData(self, session, url):
        # print(type(data))
        tmp = url.split('?')
        url = tmp[0]
        pageNo = tmp[-1:][0]
        data = {
            'province':'901',
            'district' : '', 
            'district2'  : '',
            'shopTypes'  : '',
            'payTypes'   : '',
            'cardNumFive': '',
            'shortName'  : '',
            'address': '',
            'isSupportYj': '',
            'shopMemo'   : '1',
            'pageNo': pageNo,
        }
        file = self.folder + pageNo.zfill(5)+ '.json'
        isFileExists = os.path.exists(file)
        if not isFileExists:
            async with session.post(url, headers=self.headers, data=data,timeout=15, verify_ssl=False) as response:
                print('save to .json file, page is: ' + pageNo)
                try:
                    response = await response.json()
                    with open(file, 'w') as f:
                        f.write(json.dumps(response))

                except Exception as e:
                    with open('error.log', 'w') as f:
                        f.write('error page is' + pageNo)
                    return


def test():
    import requests
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
        'Referer': 'https://www.sandpay.com.cn/shop/merchantList.html',
        'Host': 'www.sandpay.com.cn',
    }
    url = 'https://www.sandpay.com.cn/shop/getMerchantPage'
    # 1. 导入Python SSL处理模块
    import ssl
    # 2. 表示忽略未经核实的SSL证书认证
    context = ssl._create_unverified_context()
    
    data ={
        'province':'901',   # 上海市
        #'province':'902',  # 江苏省
        #'province':'903',  # 浙江省
        #'province':'904',  # 北京市
        'district' : '', 
        'district2'  : '',
        'shopTypes'  : '',
        'payTypes'   : '',
        'cardNumFive': '',
        'shortName'  : '',
        'address': '',
        'isSupportYj': '',
        'shopMemo'   : '1',
        'pageNo': '1',
    }
    r = requests.post(url, headers=headers, data=data,verify=False)

    if r.status_code == 200:  # ok
        jsonp = r.json()
        pageCount = jsonp['pageCount']

        urlList = [url+'?'+str(e) for e in range(1, int(pageCount)+1)]
        # print(urlList)
    print('All urlPage is: ', len(urlList))
    c = Crawler(urlList)
    c.folder = './data/'
    isExists = os.path.exists(c.folder)
    if not isExists:
        os.makedirs(c.folder)
    asyncio.run(c.crawl())
    print('OK')


if __name__=='__main__':
    start = time.time()
    test()
    end = time.time()
    print("Finished in Time Consuming: {}".format(end-start))

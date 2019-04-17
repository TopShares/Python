import asyncio
import time
import requests
from lxml import etree
import re
import os

class Crawler:

    def __init__(self, data, max_workers=4):
        self.datas = data
        # create a queue that only allows a maximum of two items
        self.fetching = asyncio.Queue()
        self.max_workers = max_workers

    async def crawl(self):
        # DON'T await here; start consuming things out of the queue, and
        # meanwhile execution of this function continues. We'll start two
        # coroutines for fetching and two coroutines for processing.
        all_the_coros = asyncio.gather(
            *[self._worker(i) for i in range(self.max_workers)])

        # place all URLs on the queue
        for data in self.datas:
            await self.fetching.put(data)

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

            print(f'Fetch worker {i} is fetching a URL: {url}')
            page = await self.fetch(url)
            self.process(page)

    async def fetch(self, url):
        print("Fetching URL: " + url);
        # await asyncio.sleep(2)
        return f"the contents of {url}"

    def process(self, page):
        print("processed page: " + page)




def getUrlList(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0',' WOW64) AppleWebKit/537.cipg (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"}
    html = ''
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        if r.status_code == 200:  # ok
            html = r.content.decode('gbk') 
        else:
            return None
    except:
        return None

    html = etree.HTML(html)
    folder = html.xpath('//*[@id="comicName"]/text()')
    folder = './' + folder[0]
    isExists = os.path.exists(folder)
    if not isExists:  # 目录不存在，则创建
        os.makedirs(folder)
    e = html.xpath('//*[@class="classBox autoHeight"]/div/li//a')
    data = []
    tmp = {}
    for i in e:
        tmp['url'] = 'https://m.kukukkk.com' + i.xpath('./@href')[0]
        tmp['txt'] = folder + '/' +  i.xpath('./text()')[0]
        data.append(tmp)
        tmp = {}
    return data


def test():
    url = 'https://m.kukukkk.com/comiclist/2286/'
    data = getUrlList(url)
    # main loop
    c = Crawler(data)
    # c = Crawler(['http://www.google.com',   'http://www.yahoo.com', 
    #              'http://www.cnn.com',      'http://www.gamespot.com', 
    #              'http://www.facebook.com', 'http://www.evergreen.edu',
    #              ])
    asyncio.run(c.crawl())
    print('OK')


if __name__=='__main__':
    start = time.time()
    test()
    end = time.time()
    print("Finished in Time Consuming: {}".format(end-start))
# encoding:utf-8
import re
import os
import time
import aiohttp
import asyncio
from lxml import etree

class Crawler:

    def __init__(self, urls, max_workers=4):
        self.urls = urls
        self.fetching = asyncio.Queue()
        self.max_workers = max_workers
        self.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
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

            print(f'Fetch worker {i} is fetching a URL: {url}')
           
            async with aiohttp.ClientSession() as session:
                 picUrlList = await self.fetch(session,url)
                 await self.process(picUrlList)
                 # self.DownloadImg(picUrlList)

    async def fetch(self,session, url):
        print("Fetching URL: " + url);
        html = await self.getHtmlText(session, url)
        pattern = re.compile('上一页</li><li>([\s\S]*?)</li>')
        allPage = re.findall(pattern, html)
        allPage = (allPage[0]).split('/')[1]
        picUrlList = []
        for url_i in range(1, int(allPage)+1):
            url = re.sub(r'(\d+)(?=.htm)', str(url_i), url)
            picUrlList.append(url)
        return picUrlList
        # await asyncio.sleep(2)
        # return f"the contents of {url}"

    # process pic url
    async def process(self, picUrlList):
        async with aiohttp.ClientSession() as session:
            for picUrl in picUrlList:
                html = await self.getHtmlText(session, picUrl)
                pattern = re.compile("IMG SRC='([\s\S]*?)'")
                imgUrl = re.findall(pattern, html)
                imgUrl = imgUrl[0].replace('''"''', "").replace("+", "")

                parameter_global_js = ({
                # "server0": "http://n.1whour.com/",
                # "server": "http://n.1whour.com/",
                # "m200911d": "http://n.1whour.com/",
                # "m201001d": "http://n.1whour.com/",
                'm2007':'http://m8.1whour.com/',
                })
                for _i in parameter_global_js:
                    urlPic = imgUrl.replace(str(_i), str(parameter_global_js[_i]))
                    # self.SavePic(urlPic, i['txt'])
                    await self.DownloadImg(session, urlPic)

        # print("processed page: " + picUrlList)

    # download Pic
    async def DownloadImg(self, session, picUrl):
        async with session.get(picUrl, headers=self.headers, timeout=20) as response:
            img_response = await response.read()
            # picUrl ='http://m8.1whour.com/newkuku/2019/04/13/理科生坠入情网故尝试证明_第32话/00012JK.jpg'
            tmp = picUrl.split('/')[-2:]
            folder = './' + tmp[0]
            file = folder +'/'+ tmp[1]

            isExists = os.path.exists(folder)
            if not isExists:  # 目录不存在，则创建
                os.makedirs(folder)
            with open(file, 'wb') as f:
                f.write(img_response)

    # get html text
    async def getHtmlText(self, session, url):
        async with session.get(url, headers=self.headers,timeout=20) as response:
            return await response.text(encoding='gbk')
def test():
    # main loop
    import requests

    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
}

    # url = 'https://m.kukukkk.com/comiclist/2286/'
    url = 'https://m.kukukkk.com/comiclist/2284/'
    url = 'https://m.kukukkk.com/comiclist/1733/' # 七原罪
    r = requests.get(url, headers=headers)
    if r.status_code == 200:  # ok
        html = r.content.decode('gbk')
        html = etree.HTML(html)
        e = html.xpath('//*[@class="classBox autoHeight"]/div/li//a/@href')
        urlList = ['https://m.kukukkk.com'+x for x in e]
        c = Crawler(urlList)
        asyncio.run(c.crawl())
        print('OK')


if __name__=='__main__':
    start = time.time()
    test()
    end = time.time()
    print("Finished in Time Consuming: {}".format(end-start))
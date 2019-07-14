# encoding:utf-8
import re
import os
import time
import aiohttp
import asyncio
from lxml import etree

class Crawler:

    def __init__(self, urls, max_workers=8):
        self.URL = 'https://www.uumtu.com'
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

            # print(f'Fetch worker {i} is fetching a URL: {url}')
            async with aiohttp.ClientSession() as session:
                urlList = await self.fetch(session,url)            # list
                pageUrl = await self.process(session, urlList)     # detail Url

    async def fetch(self,session, url):
        # print("Fetching URL: " + url)
        with open('./u2.log','w')as f:
            f.write(url)
        html = await self.getHtmlText(session, url)
        html = etree.HTML(html)
        url = html.xpath('//*[@id="mainbodypul"]/div/a/@href')
        urlList = ['https://www.uumtu.com'+u for u in url]
        return urlList


    async def process2(self, session, UrlList):
        for picUrlList in UrlList:
            # imgList = []
            for picUrl in picUrlList:
                print('process to: '+ picUrl)
                try:
                    html = await self.getHtmlText(session, picUrl)
                    html = etree.HTML(html)
                    img = html.xpath('//*[@class="bg-white p15 center imgac clearfix"]/a/img/@src')
                    alt = html.xpath('//*[@class="bg-white p15 center imgac clearfix"]/a/img/@alt')
                    res = {'img':img[0], 'alt':alt[0]}
                    # imgList.append(res)
                    await self.DownloadImg(session, res)
                except Exception as e:
                    print(e)


    async def process(self, session, picUrlList):
        urlList = []
        for picUrl in picUrlList:
            self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
            ,'Referer': picUrl
            }
            try:
                html = await self.getHtmlText(session, picUrl)
                rep = re.compile(r'href="/siwa/(.*?).html">末页')
                result = re.findall(rep, html)
                total = (((((result[0]).split('/'))[-1:])[0]).split('_'))
                typeNum = total[0]
                total = total[-1:][0]
                tmp = [URL+typeNum+'_'+str(e)+'.html' for e in range(1,int(total)+1)]
                urlList.append(tmp)
            except Exception as e:
                print(e)

        await self.process2(session, urlList)


    # download Pic
    async def DownloadImg(self, session, res):
        # for res in picUrlList:
        picUrl = res['img']
        alt = res['alt']
        tmp = picUrl.split('/')[-2:]
        folder = './' + tmp[0]
        file = folder +'/' + alt + tmp[1]
        isExists = os.path.exists(folder)
        if not isExists:
            os.makedirs(folder)
        isFileExists = os.path.exists(file)
        if not isFileExists:
            async with session.get(picUrl, headers=self.headers, timeout=15, verify_ssl=False) as response:
                print('download picUrl: ' + picUrl)
                try:
                    img_response = await response.read()
                    with open(file, 'wb') as f:
                        f.write(img_response)
                except Exception as e:
                    print(e)
                    pass
    # get html text
    async def getHtmlText(self, session, url):
        async with session.get(url, headers=self.headers,timeout=15,verify_ssl=False) as response:
            return await response.text(encoding='utf-8')


URL = 'https://www.uumtu.com/siwa/'
def startUrls():
    import requests

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
    }
    html = requests.get(URL,headers=headers)
    rep = re.compile(r'href="/siwa/(.*?).html">末页')
    result = re.findall(rep, html.text)
    total = (((((result[0]).split('/'))[-1:])[0]).split('_'))
    typeNum = total[0]
    total = total[-1:][0]
    print('total:' + total)
    total =1
    urlList = [URL+typeNum+'_'+str(e)+'.html' for e in range(1,int(total)+1)]
    return urlList

def test():
    # main loop
    urlList = startUrls()
    c = Crawler(urlList)
    asyncio.run(c.crawl())
    print('OK')

if __name__=='__main__':
    start = time.time()
    test()
    end = time.time()
    print("Finished in Time Consuming: {}".format(end-start))

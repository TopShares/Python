# encoding:utf-8
import re
import os
import time
import aiohttp
import asyncio
from lxml import etree

class Crawler:

    def __init__(self, urls, max_workers=8):
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
                picPageUrlList = await self.fetch(session,url)
                # picUrlList = await self.process(session, picPageUrlList)
                # await self.DownloadImg(session, picUrlList)

    async def fetch(self,session, url):
        # print("Fetching URL: " + url);
        html = await self.getHtmlText(session, url)
        pattern = re.compile('上一页</li><li>([\s\S]*?)</li>')
        allPage = re.findall(pattern, html)
        allPage = (allPage[0]).split('/')[1]
        picUrlList = []
        for url_i in range(1, int(allPage)+1):
            url = re.sub(r'(\d+)(?=.htm)', str(url_i), url)
            picUrlList.append(url)
        return picUrlList

    # process pic url
    async def process(self, session, picUrlList):
        # print("process URL: " + picUrlList)

        html = await self.getHtmlText(session, picUrlList)
        # pattern = re.compile("IMG SRC=\"(.*?)'",re.IGNORECASE)
        pattern = re.compile(r'<img src="(.*?)" alt="(.*?)" />')
        imgUrl = re.findall(pattern, html)
        return imgUrl[0][0]
        # tmp = []
        # for picUrl in picUrlList:
        #     print("process picUrl: " + picUrl)
        #     exit()
        #     html = await self.getHtmlText(session, picUrl)
        #     print(html)
        #     pattern = re.compile("IMG SRC='([\s\S]*?)'",re.IGNORECASE)
        #     # pattern = re.compile(r'<img src="(.*?)" alt="(.*?)" />')
        #     imgUrl = re.findall(pattern, html)
        #     print(imgUrl)
        #     exit()
        #     imgUrl = imgUrl[0].replace('''"''', "").replace("+", "")

        #     parameter_global_js = ({
        #     # "server0": "http://n.1whour.com/",
        #     # "server": "http://n.1whour.com/",
        #     # "m200911d": "http://n.1whour.com/",
        #     # "m201001d": "http://n.1whour.com/",
        #     'm2007':'http://m8.1whour.com/',
        #     })
        #     for _i in parameter_global_js:
        #         urlPic = imgUrl.replace(str(_i), str(parameter_global_js[_i]))
        #         tmp.append(urlPic)
        # return tmp

    # download Pic
    async def DownloadImg(self, session, picUrlList):
        for picUrl in picUrlList:
            async with session.get(picUrl, headers=self.headers, timeout=15, verify_ssl=False) as response:
                print('download picUrl: ' + picUrl)
                try:
                    img_response = await response.read()
                    tmp = picUrl.split('/')[-2:]
                    folder = './' + tmp[0]
                    file = folder +'/'+ tmp[1]

                    isExists = os.path.exists(folder)
                    if not isExists:
                        os.makedirs(folder)
                    with open(file, 'wb') as f:
                        f.write(img_response)
                except Exception as e:
                    print(e)
                    pass

    # get html text
    async def getHtmlText(self, session, url):
        print(url)
        async with session.get(url, headers=self.headers,timeout=15,verify_ssl=False) as response:
            return await response.text(encoding='utf-8')



def test():
    # main loop
    import requests

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
    }

    URL = 'https://www.uumtu.com/siwa/'
    image_url = "https://www.uumtu.com/siwa/28470.html"
    # html = requests.get(image_url, headers=headers)
    # rep = re.compile(r'<img src="(.*?)" alt="(.*?)" />')
    # result = re.findall(rep, html.text)

    html = requests.get(image_url,headers=headers)
    rep = re.compile(r'href="/siwa/(.*?).html">末页')
    result = re.findall(rep, html.text)
    total = (((((result[0]).split('/'))[-1:])[0]).split('_'))
    typeNum = total[0]
    total = total[-1:][0]
    go = 1
    
    urlList = [URL+typeNum+'_'+str(e)+'.html' for e in range(1,int(total)+1)]
    c = Crawler(urlList)
    asyncio.run(c.crawl())
    print('OK')

if __name__=='__main__':
    start = time.time()
    test()
    end = time.time()
    print("Finished in Time Consuming: {}".format(end-start))

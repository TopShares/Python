import aiohttp
import asyncio
import time
import json
import re

class Crawler:

    def __init__(self, urls, max_workers=8):
        self.urls = urls
        # create a queue that only allows a maximum of two items
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
                await self.fetch(session,url)


    async def fetch(self,session,  url):
        print("Fetching URL: " + url)
        html = await self.getHtmlText(session, url)
        pattern = re.compile(
            '<i class="board-index board-index-\d+">([\s\S]*?)</i>'
            '[\s\S]*?<p class="name">.*?title="([\s\S]*?)"'
            '[\s\S]*?<p class="star">([\s\S]*?)</p>'
            '[\s\S]*?<p class="releasetime">([\s\S]*?)</p>')
        items = re.findall(pattern, html)
        for item in items:
            ele = {
            'board-index': item[0].strip(),
            'title': item[1].strip(),
            'actor': item[2].strip(),
            'time': item[3].strip(),
            }
            with open("MaoYanMovie.txt", 'a', encoding='utf-8') as f:
                # json encode -> json str
                f.write(json.dumps(ele, ensure_ascii=False) + '\n')


    # get html text
    async def getHtmlText(self, session, url):
        async with session.get(url, headers=self.headers,timeout=15,verify_ssl=False) as response:
            return await response.text(encoding='utf-8')
            

def test():
    # main loop
    urlList = ['http://maoyan.com/board/4?offset=' + str(offset * 10) for offset in range(10)]
    c = Crawler(urlList)
    asyncio.run(c.crawl())
    print('OK')


if __name__=='__main__':
    start = time.time()
    open('MaoYanMovie.txt','w',encoding='utf-8')
    test()
    end = time.time()
    print("Finished in Time Consuming: {}".format(end-start))
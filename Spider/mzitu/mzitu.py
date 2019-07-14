import aiohttp
import asyncio
import time
from lxml import etree

class Crawler:

    def __init__(self, urls, max_workers=4):
        self.urls = urls
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
            page = await self.fetch(url)
            self.process(page)

    async def fetch(self, url):
        print("Fetching URL: " + url);
        # await asyncio.sleep(2)
        return f"the contents of {url}"

    def process(self, page):
        print("processed page: " + page)

    # get html text
    async def getHtmlText(self, session, url):
        async with session.get(url, headers=self.headers,timeout=15,verify_ssl=False) as response:
            return await response.text(encoding='utf-8')

import requests
def get_urls():
    """
    获取 mzitu 网站下所有套图的 url
    """
    HEADERS = {
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Referer': 'http://www.mzitu.com'
    }
    html = etree.HTML(requests.get('http://www.mzitu.com', headers=HEADERS, timeout=10).text)
    pageNumbers = html.xpath('//*[@class="page-numbers"]//text()')
    allPage = max(list(map(lambda x:int(x), pageNumbers)))
    page_urls = ['http://www.mzitu.com/page/{cnt}'.format(cnt=cnt)
                 for cnt in range(1, allPage)]
    print(allPage)
    print("Please wait for second ...")
    return page_urls
    # img_urls = []
    # for page_url in page_urls:
    #     try:
    #         html = etree.HTML(requests.get(page_url, headers=HEADERS, timeout=10).text)
    #         img_urls.extend(html.xpath('//*[@id="pins"]/li/a//@href'))
    #     except Exception as e:
    #         print(e)
    # return img_urls

def test():
    # main loop
    get_urls()
    # c = Crawler(imgUrls)
    # asyncio.run(c.crawl())
    # print('OK')


if __name__=='__main__':
    start = time.time()
    test()
    end = time.time()
    print("Finished in Time Consuming: {}".format(end-start))
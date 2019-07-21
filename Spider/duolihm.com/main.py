#!/usr/bin/env python3

import asyncio
import logging
import re
import signal
import sys
import urllib.parse
from lxml import etree

import aiohttp


class Crawler:

    def __init__(self, rooturl, loop, maxtasks=100):
        self.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
        }
        from urllib.parse import urlsplit

        result = urlsplit(rooturl)
        """
        (scheme='https'（协议）, netloc='www.duolihm.com'（域）, 
        path='/daxuesheng'（路径）, params=''（可选参数）, 
        query='name=zhangsan'（查询参数）, fragment='123'（锚点）)
        """
        self.BaseURL = result.scheme+"//" + result.netloc
        self.rooturl = rooturl
        self.loop = loop
        self.todo = set()
        self.busy = set()
        self.done = {}
        self.tasks = set()
        self.sem = asyncio.Semaphore(maxtasks, loop=loop)

        # connector stores cookies between requests and uses connection pool
        self.session = aiohttp.ClientSession(loop=loop,headers=self.headers)

    async def run(self):
        t = asyncio.ensure_future(self.addurls([(self.rooturl, '')],'P'), loop=self.loop)
        await asyncio.sleep(1, loop=self.loop)
        while self.busy:
            await asyncio.sleep(1, loop=self.loop)

        await t
        await self.session.close()
        self.loop.stop()

    async def addurls(self, urls, flag):
        for url, parenturl in urls:
            url = urllib.parse.urljoin(parenturl, url)
            url, frag = urllib.parse.urldefrag(url)
            print(url)
            if (#url.startswith(self.rooturl) and
                    url not in self.busy and
                    url not in self.done and
                    url not in self.todo):
                self.todo.add(url)
                print( 'add... '+ url)
                await self.sem.acquire()
                if flag == 'P':
                    task = asyncio.ensure_future(self.process(url), loop=self.loop)
                else:
                    task = asyncio.ensure_future(self.detial_page(url), loop=self.loop)

                task.add_done_callback(lambda t: self.sem.release())
                task.add_done_callback(self.tasks.remove)
                self.tasks.add(task)

    async def process(self, url):
        print('processing:', url)

        self.todo.remove(url)
        self.busy.add(url)
        try:
            resp = await self.session.get(url)
        except Exception as exc:
            print('...', url, 'has error', repr(str(exc)))
            self.done[url] = False
        else:
            if (resp.status == 200 and  ('text/html' in resp.headers.get('content-type'))):
                data = (await resp.read()).decode('utf-8', 'replace')
                tree = etree.HTML(data)
                urls = tree.xpath('//*[@id="detail-list-select"]/li/a//@href')
                # urls = [ self.BaseURL + e for e in urls]
                # urls = re.findall(r'(?i)href=["\']?([^\s"\'<>]+)', data) 
                asyncio.Task(self.addurls([(u, url) for u in urls], 'Q'))

            resp.close()
            self.done[url] = True

        # self.busy.remove(url)
        # print(len(self.done), 'completed tasks,', len(self.tasks),
        #       'still pending, todo', len(self.todo))

    async def detial_page(self, url):
        print('detail page processing:', url)

        self.todo.remove(url)
        self.busy.add(url)
        try:
            resp = await self.session.get(url)
        except Exception as exc:
            print('...', url, 'has error', repr(str(exc)))
            self.done[url] = False
        else:
            if (resp.status == 200 and  ('text/html' in resp.headers.get('content-type'))):
                data = (await resp.read()).decode('utf-8', 'replace')
                tree = etree.HTML(data)
                imgUrls = tree.xpath('//*[@class="comicpage"]//div//img//@src')
                print(imgUrls)
                # urls = [ self.BaseURL + e for e in urls]
                # urls = re.findall(r'(?i)href=["\']?([^\s"\'<>]+)', data) 
                # asyncio.Task(self.addurls([(u, url) for u in urls], 'Q'))

            resp.close()
            self.done[url] = True

        self.busy.remove(url)
        print(len(self.done), 'completed tasks,', len(self.tasks),
              'still pending, todo', len(self.todo))


def main():
    loop = asyncio.get_event_loop()
    baseUrl = 'https://www.duolihm.com/book/607'
    c = Crawler(baseUrl, loop)
    asyncio.ensure_future(c.run(), loop=loop)

    try:
        loop.add_signal_handler(signal.SIGINT, loop.stop)
    except RuntimeError:
        pass
    loop.run_forever()
    print('todo:', len(c.todo))
    print('busy:', len(c.busy))
    print('done:', len(c.done), '; ok:', sum(c.done.values()))
    print('tasks:', len(c.tasks))


if __name__ == '__main__':
    import time
    t1 = time.time()
    main()
    print("total time: ", time.time() - t1)

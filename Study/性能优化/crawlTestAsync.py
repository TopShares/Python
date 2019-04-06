import aiohttp
import asyncio
import time
# from bs4 import BeautifulSoup
from urllib.request import urljoin
import re
import requests
import multiprocessing as mp

# base_url = "https://manhua.fzdm.com/"

# 七大罪
base_url = 'https://manhua.fzdm.com/56/'
        
seen = set()
unseen = set([base_url])


def parse(html):
    rep = re.compile('pure-u-lg-1-4">([\s\S]*?)</li>')
    content = re.findall(rep, html)
    # <a href="018/" title="七原罪018话">七原罪018话</a>
    title,page_urls = [], []
    for i in content:
        res= re.findall(r'href="(.*?)" title="(.*?)"',i)
        p,t = res[0]
        title.append(t)
        page_urls.append(base_url + p)
    return title, page_urls
    # soup = BeautifulSoup(html, 'lxml')
    # urls = soup.find_all('a', {"href": re.compile('^/.+?/$')})
    # title = soup.find('h1').get_text().strip()
    # page_urls = set([urljoin(base_url, url['href']) for url in urls])
    # url = soup.find('meta', {'property': "og:url"})['content']

    # print(r)
    # return title, page_urls, url


async def crawl(url, session):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    r = await session.get(url,headers=headers)
    html = await r.text()
    await asyncio.sleep(0.1)        # slightly delay for downloading
    return html


async def main(loop):
    pool = mp.Pool(4)               # slightly affected
    async with aiohttp.ClientSession() as session:
        while len(unseen) != 0:
            print('\nAsync Crawling...')
            tasks = [loop.create_task(crawl(url, session)) for url in unseen]
            finished, unfinished = await asyncio.wait(tasks)
            htmls = [f.result() for f in finished]  
            
            print('\nDistributed Parsing...')
            parse_jobs = [pool.apply_async(parse, args=(html,)) for html in htmls]
            results = [j.get() for j in parse_jobs]
            # second_parse = [pool.apply_async(pare, args())]

            
            print('\nAnalysing...')
            seen.update(unseen)
            unseen.clear()
            for title, page_urls in results:
                print(title,page_urls)
                # unseen.update(page_urls - seen)

if __name__ == "__main__":
    t1 = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    # loop.close()
    print("Async total time: ", time.time() - t1)

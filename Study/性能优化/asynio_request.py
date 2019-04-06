import asyncio
import requests


@asyncio.coroutine
def fetch_async(func, *args):
    loop = asyncio.get_event_loop()
    future = loop.run_in_executor(None, func, *args)
    response = yield from future
    print(type(response))
    print(dir(response))
    response.encoding='utf-8'
    print(response.text)
    print(response.url)
    # print(response.url, response.content)


#给request设置编码为UTF-8
#必须在调用所有getParameter之前
# request.setCharacterEncoding("UTF-8");

headers = {
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
}

tasks = [
    fetch_async(requests.get,'https://manhua.fzdm.com/56/295/index_0.html'),
    # fetch_async(requests.get, 'http://www.baidu.com/')
]

loop = asyncio.get_event_loop()
results = loop.run_until_complete(asyncio.gather(*tasks))
loop.close()

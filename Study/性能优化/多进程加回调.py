from concurrent.futures import ProcessPoolExecutor
import requests


def fetch_async(url):
    response = requests.get(url)
    return response


def callback(future):
    print(future.result())


url_list = ['http://www.github.com', 'http://www.bing.com']
pool = ProcessPoolExecutor(5)
for url in url_list:
    v = pool.submit(fetch_async, url)
    v.add_done_callback(callback)
pool.shutdown(wait=True)
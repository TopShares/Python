from concurrent.futures import ThreadPoolExecutor
import requests


def fetch_async(url):
    response = requests.get(url)
    return response


url_list = ['http://www.github.com', 'http://www.bing.com']
pool = ThreadPoolExecutor(5)
for url in url_list:
    pool.submit(fetch_async, url)
pool.shutdown(wait=True)
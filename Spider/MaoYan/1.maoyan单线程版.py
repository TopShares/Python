import requests
import json
import random
import re
import time
from multiprocessing import Pool
import functools


def get_one_page(url):
    """
    发起Http请求，获取Response的响应结果
    """
    ua_headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"}
    reponse = requests.get(url, headers=ua_headers)
    if reponse.status_code == 200:  # ok
        return reponse.text
    return None


def write_to_file(item):
    """
    把抓取到的数据写入本地文件
    """
    with open("猫眼电影.txt", 'a', encoding='utf-8') as f:
        # json encode -> json str
        f.write(json.dumps(item, ensure_ascii=False) + '\n')


def parse_one_page(html):
    """
    从获取到的html页面中提取真实想要存储的数据：
    电影名，主演，上映时间
    """
    pattern = re.compile(
        '<i class="board-index board-index-\d+">([\s\S]*?)</i>'
        '[\s\S]*?<p class="name">.*?title="([\s\S]*?)"'
        '[\s\S]*?<p class="star">([\s\S]*?)</p>'
        '[\s\S]*?<p class="releasetime">([\s\S]*?)</p>')
    items = re.findall(pattern, html)

    # yield在返回的时候会保存当前的函数执行状态
    for item in items:
        yield {
            'board-index': item[0].strip(),
            'title': item[1].strip(),
            'actor': item[2].strip(),
            'time': item[3].strip(),
        }

def CrawlMovieInfo(lock, offset):
    """
    抓取电影的电影名，主演，上映时间
    """
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    print(url)
    # 抓取当前的页面
    html = get_one_page(url)
    # print(html)

    # 这里的for
    for item in parse_one_page(html):
        lock.acquire()
        write_to_file(item)
        lock.release()

    # 每次下载完一个页面，随机等待1-3秒再次去抓取下一个页面
    # time.sleep(random.randint(1,3))


if __name__ == "__main__":
    start_time = time.time()
    open('猫眼电影.txt','w',encoding='utf-8')

    # 把页面做10次的抓取，每一个页面都是一个独立的入口
    from multiprocessing import Manager

    # from multiprocessing import Lock 进程池中不能用这个lock

    # 进程池之间的lock需要用Manager中lock
    manager = Manager()
    lock = manager.Lock()

    # 使用 functools.partial对函数做一层包装,从而把这把锁传递进进程池
    # 这样进程池内就有一把锁可以控制执行流程
    partial_CrawlMovieInfo = functools.partial(CrawlMovieInfo, lock)
    pool = Pool()
    pool.map(partial_CrawlMovieInfo, [i * 10 for i in range(10)])

    pool.close()
    pool.join()

#    for i in range(10):
#        CrawlMovieInfo(i*10) #offset -> 0,10,20,...90


    seconds = time.time() - start_time
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    print("用时：%02d:%02d:%04fs" % (h, m, s))
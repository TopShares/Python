#!/usr/bin/env python
# coding=utf-8

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from gevent.pool import Pool
from gevent import monkey, sleep
import requests
from queue import Queue
from conf.config import config
import os
import hashlib
import logging
from umei import *


monkey.patch_all()

c = config()
c.db_conf('mongodb://localhost:27017', db='umei_net', collection='umei2')

browser = c.browser
mongodb = c.mongodb
imgInfo = {
    'ParentPage': '',
    'ParentUrl': '',
    'ArticleTitle': '',
    'ArticleTime': '',
    'ArticleGenre': '',
    'ImageUrl': []
}


class Config:

    # 线程池容量
    POOL_MAXSIZE = 512
    # worker 数量
    WORKERS_MAXSIZE = 16
    # 每次请求延迟（秒）
    DELAY_TIME = 0.25
    # 请求超时时间（秒）
    REQUEST_TIMEOUT = 8
    # 每个链接重试次数
    MAX_RETRIES = 5
    # 日志等级
    LOG_LEVEL = logging.INFO

    URLS_DATA = "data.txt"
    PICS_DIR = "pics"
    PICS_EXT = ".jpg"
    PICS_FILENAME_LENGTH = 16

    USER_AGENT = (
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    )


CONFIG = Config()


class Logger:

    @staticmethod
    def get():
        formatter = logging.Formatter("%(asctime)s - %(message)s")
        logger = logging.getLogger("monitor")
        logger.setLevel(CONFIG.LOG_LEVEL)
        sh = logging.StreamHandler()
        sh.setFormatter(formatter)
        handler = logging.FileHandler("log.txt")
        handler.setLevel(CONFIG.LOG_LEVEL)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.addHandler(sh)
        return logger


class Downloader:

    def __init__(self):
        self.urls_queue = Queue()
        self.pool = Pool(CONFIG.POOL_MAXSIZE)
        self.logger = Logger.get()
        self.init_queue()
        self.create_dir()

    def init_queue(self):
        """
        初始化队列，导入数据
        """
        url = 'https://www.umei.net/touxiangtupian/feizhuliutouxiang/index.htm'  # 非主流头像
        url = 'https://www.umei.net/faxingtupian/mingxingfaxing/index.htm'  # 明星发型
        # allPage = get_all_page(url)
        allPage = 2
        urls = joint_url(url, allPage)
        for x in urls:
            self.urls_queue.put({x.strip(): CONFIG.MAX_RETRIES})

    @staticmethod
    def create_dir():
        """
        如果文件夹不存在，则创建文件夹
        """
        if not os.path.exists(CONFIG.PICS_DIR):
            os.mkdir(CONFIG.PICS_DIR)

    @staticmethod
    def headers(url):
        """
        根据对应 url 返回 headers
        """
        if url.startswith("https://kr.shanghai-jiuxin.com/"):
            return {
                "User-Agent": CONFIG.USER_AGENT,
                "Referer": "https://kr.shanghai-jiuxin.com/"
            }

    @staticmethod
    def get_URL_EXT(url):
        #  url = "http://distilleryimage2.instagram.com/da4ca3509a7b11e19e4a12313813ffc0_7.jpg"
        filename = os.path.basename(url)
        from pathlib import Path
        return Path(filename).suffix

    def parse_imgUrls(url, page):
        '''
        解析图片页面上的链接
        '''
        print("FFFFF: " + url)
        browser.get(url)
        wait = WebDriverWait(browser, 3)
        imgUrl = wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, '.TypeBigPics')))
        dataList = []
        for i in imgUrl:
            url = i.get_attribute('href').strip()
            tmp = {'page': page, 'url': url}
            dataList.append(tmp)
        print(dataList)
        print("okkk")
        return dataList

    def download(self):
        while True:
            sleep(CONFIG.DELAY_TIME)

            for url, num in self.urls_queue.get().items():
                # 队列大小
                self.logger.warning("Jobs: {}".format(
                    str(self.urls_queue.qsize())))
                if num <= 0:
                    # For each get() used to fetch a task, a subsequent call
                    # to task_done() tells the queue that the processing on
                    # the task is complete.
                    self.urls_queue.task_done()
                    break
                try:
                    file_name = os.path.basename(url)
                    page = file_name.split('_')[-1].split('.')[0]
                    if page == 'index':
                        page = 1

                    self.logger.info("url: " + url)
                    self.logger.info(parse_imgUrls(url, int(page)))

                except Exception as e:
                    self.logger.error(e)
                    if num >= 1:
                        self.urls_queue.put({url: num - 1})
                        self.logger.warning(
                            "Url: {} retry times {}".format(
                                url, CONFIG.MAX_RETRIES - (num - 1))
                        )
                finally:
                    self.urls_queue.task_done()  # 确保最后总会执行 task_done()
                    self.logger.info("done...")

    def execute_workers(self, target):
        """
        启动 workers
        """
        for i in range(CONFIG.WORKERS_MAXSIZE):
            self.pool.apply_async(target)

    def run(self):
        """
        运行主函数，用于启动队列
        """
        self.execute_workers(self.download)
        # If a join() is currently blocking, it will resume when all items
        # have been processed (meaning that a task_done() call was received
        # for every item that had been put() into the queue).
        self.urls_queue.join()


if __name__ == "__main__":
    c.selenium_conf(headless=True)
    try:
        downloader = Downloader()
        downloader.run()
    except KeyboardInterrupt:
        print("You have canceled all jobs.")

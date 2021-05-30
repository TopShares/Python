
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from contextlib import suppress
import selenium
from conf.db import MongoDB
from selenium.webdriver.common.action_chains import ActionChains
from common.randomUtil import time_sleep
from conf.config import config
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import WebDriverWait

c = config()
c.db_conf('mongodb://localhost:27017', db='umei_net', collection='umei')

browser = c.browser
mongodb = c.mongodb

imgData = []
imgInfo = {
    'ParentPage': '',
    'ParentUrl': '',
    'ArticleTitle': '',
    'ArticleTime': '',
    'ArticleGenre': '',
    'ImageUrl': []
}


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


def parse_imgUrl(page, url):
    '''
    解析链接上的图片地址并下载
    '''
    pageCount = get_all_page(url)

    if pageCount == None:
        pageCount = '1'

    imgInfo['ParentPage'] = page
    imgInfo['ParentUrl'] = url
    # 拼接url
    urls = joint_url(url, int(pageCount))
    download_img(urls)


def get_img_info(wait):
    # body > div.wrap > div.ArticleTitle > strong
    ArticleTitle = wait.until(EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, 'body > div.wrap > div.ArticleTitle > strong')))[0]
    imgInfo['ArticleTitle'] = ArticleTitle.text

    ArticleTime = wait.until(EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, 'body > div.wrap > div.ArticleInfos > span.time')))[0]
    imgInfo['ArticleTime'] = ArticleTime.text

    ArticleGenre = wait.until(EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, 'body > div.wrap > div.ArticleInfos > span.column > a')))[0]
    imgInfo['ArticleGenre'] = ArticleGenre.text


def download_img(urls):
    '''
    每页都包含img，下载
    '''
    # 图片url
    # #ArticleId\{dede\:field\.reid\/\}
    # .ImageBody > p > img
    for url in urls:
        browser.get(url)
        # with suppress(TimeoutException, NoSuchElementException):
        try:
            browser.execute_script(
                "window.scrollTo(0,document.body.scrollHeight);")  # 下划网页至底部
            wait = WebDriverWait(browser, 10)
            selector = '.ImageBody > p > img'
            imgUrl = wait.until(EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, selector)))
            # https://www.umei.net/touxiangtupian/QQtouxiang/231824.htm
            for i in imgUrl:
                href = i.get_attribute('src').strip()
                imgInfo['ImageUrl'].append(href)
        except(TimeoutException, NoSuchElementException):
            # 多张图片
            try:
                browser.execute_script(
                    "window.scrollTo(0,document.body.scrollHeight);")
                wait = WebDriverWait(browser, 10)
                selector = '.ImageBody > p > strong > img'
                imgUrl = wait.until(EC.presence_of_all_elements_located(
                    (By.CSS_SELECTOR, selector)))
                for i in imgUrl:
                    href = i.get_attribute('src').strip()
                    imgInfo['ImageUrl'].append(href)
            except(TimeoutException):
                try:
                    browser.execute_script(
                        "window.scrollTo(0,document.body.scrollHeight);")
                    wait = WebDriverWait(browser, 10)
                    selector = '.ImageBody > img'
                    imgUrl = wait.until(EC.presence_of_all_elements_located(
                        (By.CSS_SELECTOR, selector)))
                    for i in imgUrl:
                        href = i.get_attribute('src').strip()
                        imgInfo['ImageUrl'].append(href)
                except(TimeoutException):
                    pass

        finally:
            get_img_info(wait)

    # imgData.append(imgInfo)
    imgInfo["_id"] = mongodb.create_id()
    mongodb.insert(imgInfo)
    imgInfo['ImageUrl'] = []
    # time_sleep(5)
    # time.sleep(0.25)

    # http://kr.shanghai-jiuxin.com/file/2021/0430/99bc220c184543c71c5e76b5bd0ae523.jpg


def joint_url(url, endPage):
    '''
    传入url, 迭代拼接url
    '''
    # url
    # https://www.umei.net/touxiangtupian/QQtouxiang/231824.htm
    urls = []
    urls.append(url)
    for i in range(2, int(endPage)+1):
        a = '_' + str(i) + '.htm'
        tmp = url.replace('.htm', a)
        urls.append(tmp)
    return urls


def get_all_page(url):
    '''
    获取url中的链接地址
    '''
    # td:last-child 取最后一个结点
    # body > div.wrap > div.NewPages > a:nth-child(12)
    browser.get(url)
    wait = WebDriverWait(browser, 3)
    selector = 'body > div.wrap > div.NewPages > a:last-child'

    with suppress(TimeoutException, NoSuchElementException):
        allPage = wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, selector)))[0]
        href = allPage.get_attribute('href').strip()
        pageCount = href.split('_')[-1].split('.')[0]
        return pageCount


def test_url():
    url = 'https://www.umei.net/touxiangtupian/QQtouxiang/231359.htm'
    url = 'https://www.umei.net/touxiangtupian/QQtouxiang/231357.htm'
    url = 'https://www.umei.net/touxiangtupian/QQtouxiang/231162.htm'
    parse_imgUrl(url)


def test():
    imgInfo = {
        'ArticleTitle': '',
        'ArticleTime': '',
        'ArticleGenre': '',
        'ImageUrl': []
    }
    for i in range(1, 5):
        imgInfo['ImageUrl'].append(i)
    # tmp = mongodb.create_id()
    imgInfo['_id'] = mongodb.create_id()
    mongodb.insert(imgInfo)

    for i in range(2, 5):
        imgInfo['ImageUrl'].append(i)
    imgInfo['_id'] = mongodb.create_id()
    mongodb.insert(imgInfo)


def db_test():
    mongodb.insert({'test': 'test'})


if __name__ == '__main__':
    # test()
    # test_url()
    # db_test()
    # exit()

    # 单线程下载
    c.selenium_conf(headless=True)

    url = 'https://www.umei.net/touxiangtupian/QQtouxiang/index.htm'
    url = 'https://www.umei.net/touxiangtupian/feizhuliutouxiang/index.htm'  # 非主流头像
    allPage = get_all_page(url)
    urls = joint_url(url, allPage)

    allUrlList = []

    count = 1
    for u in urls:
        print("now count: " + str(count))
        [allUrlList.append(x) for x in parse_imgUrls(u, count)]
        count += 1
    [parse_imgUrl(x['page'], x['url']) for x in allUrlList]

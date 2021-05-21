from conf.config import config
import time

c = config()

c.selenium_conf(headless=False)
browser = c.browser
url = 'http://127.0.0.1:5211/'
browser.get(url)
time.sleep(10)



def get_all_page():
    pass



def next_page(page_number):
    '''
    翻页
    '''
    pass

def pic_download(urls):
    '''
    图片下载
    '''
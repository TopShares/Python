from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time,os,json
import urllib.parse 
from selenium.webdriver import ActionChains

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from lxml import etree

import urllib.parse


import myPyMongodb

class Crawler:

    def __init__(self, rooturl):
        self.db = myPyMongodb.myMongodb(host='127.0.0.1',port=27017,database='my_database',collection='fzdm_') 
        self.rooturl = rooturl

        # 参数对象， 控制Chrome以无界面模式打开
        self.chrome_options = Options()
        self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument('--disable-gpu')

        path = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        path = r'C:\Users\liu.banglong\AppData\Local\Google\Chrome\Application\chromedriver.exe'
        abspath = os.path.abspath(path) 
        
        # 创建浏览器对象
        self.browser = webdriver.Chrome(executable_path=abspath,chrome_options=self.chrome_options)

    def run(self):
        urlist = self.parse()
        self.browser.quit()

    def parse(self):
        self.browser.get(self.rooturl)
        wait = WebDriverWait(self.browser, 3)
        # result = self.browser.find_element_by_xpath('//*[@id="content"]//li//a/@href')
        try:
            wait.until(EC.presence_of_element_located((By.ID, "content")))
            html = self.browser.page_source
            html = etree.HTML(html)
            
            res = html.xpath('//*[@id="content"]//li//a')
            li = []
            id = 334
            for td in res:
                txt = td.xpath('.//text()')[0]
                url = td.xpath('.//@href')[0]
                url = urllib.parse.urljoin(self.rooturl, url)
                
                tmp = {'txt':txt, 'url':url, 'id': str(id).zfill(3)}
                id -= 1
                li.append(tmp)
            print(li)
            self.db.insert_data_many(li)
            # res = self.browser.find_element_by_class_name('pure-u-1-2 pure-u-lg-1-4')
            # res = self.browser.find_element_by_css_selector('#content > li')
            # res = self.browser.find_element_by_xpath('//*[@id="content"]//li//a/@href')

        except Exception as e:
            print(e)
            self.browser.quit()






def main():
    baseUrl = 'https://manhua.fzdm.com/56/'   # 七原罪
    c = Crawler(baseUrl)
    c.run()

if __name__ == "__main__":
    start = time.time()
    main()
    print("total time: ", time.time() - start)
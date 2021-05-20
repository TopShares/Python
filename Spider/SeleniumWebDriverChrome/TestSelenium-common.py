# -*- coding:utf-8 -*-
from selenium import webdriver
import os
import time
import re
from selenium.webdriver.common.by import By
# from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from pyquery import PyQuery as pq


from selenium.webdriver import ChromeOptions
option = ChromeOptions()
option.add_argument('--headless')

from selenium.common.exceptions import TimeoutException
abspath = os.path.abspath(r"C:\Program Files\Google\Chrome\Application\chromedriver.exe")
browser = webdriver.Chrome(abspath,options=option)

# browser = webdriver.Chrome()

'''
find_element_by_name
find_element_by_id
find_element_by_xpath
find_element_by_link_text
find_element_by_partial_link_text
find_element_by_tag_name
find_element_by_class_name
find_element_by_css_selector
'''
# url = 'https://www.baidu.com'
# browser.get(url)
# input_str = browser.find_element(By.ID,"kw")

# input_str.send_keys("ipad")
# time.sleep(1)
# input_str.clear()
# input_str.send_keys("MakBook pro")
# button = browser.find_element(By.ID,'su')
# button.click()

# time.sleep(2)

# # 将动作附加到动作链中串行执行
# url = "http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# source = browser.find_element_by_css_selector('#draggable')
# target = browser.find_element_by_css_selector('#droppable')
# actions = ActionChains(browser)
# actions.drag_and_drop(source, target)
# actions.perform()

# # exec javaScript
# browser.get("http://www.zhihu.com/explore")
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# browser.execute_script('alert("To Bottom")')

# # 获取ID，位置，标签名
# url = 'https://www.zhihu.com/explore'
# browser.get(url)
# input = browser.find_element_by_class_name('zu-top-add-question')
# print(input.id)
# print(input.location)
# print(input.tag_name)
# print(input.size)

# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# source = browser.find_element_by_css_selector('#draggable')
# print(source)
# try:
#     logo = browser.find_element_by_class_name('logo')
# except NoSuchElementException:
#     print('NO LOGO')
# browser.switch_to.parent_frame()
# logo = browser.find_element_by_class_name('logo')
# print(logo)
# print(logo.text)

# url = 'http://www.hao6v.com/gvod/zx.html'
# '''
# 获取最新的电影
# '''
# browser.get(url)
# list1 = browser.find_element(By.XPATH,'//*[@id="main"]/div[1]/div/ul/li[1]/a')
# list1 =list1.get_attribute("href")
# print(list1)

# url = 'https://www.zhongziso.com/'
# wait = WebDriverWait(browser, 10)
#
# def search():
#     try:
#         browser.get(url)
#         input = wait.until(
#             EC.presence_of_element_located((By.CSS_SELECTOR, "#search"))
#             )
#         submit = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#topsearch > fieldset > div > div > span > button")))
#         input.send_keys('电影')
#         submit.click()
#         submit = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#topsearch > fieldset > div > div > span > button")))
#     except TimeoutException:
#         return search
#


# def next_page(page_number):
#     '''
#     翻页
#     '''
#     pass


wait = WebDriverWait(browser, 3)

def search(KEYWORD):
    url = 'https://www.javbus.cc/'
    url = url + KEYWORD
    try:
        print(url)
        browser.get(url)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#magnet-table")))
        html = browser.page_source
        doc = pq(html)
        table = doc("#magnet-table")
        table = str(table)
        Magnet = re.findall(r'width="70%" onclick="window.open\(\'(.*?)&amp;', table, re.S)
        with open('Torrent.txt', 'a', encoding="utf-8") as f:
            for i in Magnet:
                f.write(i+"\n")

        # for item in table('tr'):        #     # 这个循环循环多次,item是html的对象
        #     print(item)
        # print(doc("#magnet-table"))
        # for item in doc("#magnet-table").items():
        #     print(item)
    except TimeoutException:
        return
    finally:
        return

def getMagnet():
    pass

def main():
    # filename = "main.txt"
    # if os.path.exists(filename):
    #     with open(filename, 'r', encoding="utf-8") as f:
    #         for line in f:
    #             word = line.strip('\n')
    #             search(word)
    word='丝'
    url = 'https://sdasdasertre.xyz/forum-2-1.html'
    browser.get(url)
    total = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#fd_page_top > div > label > span')))
    for i in total:
        print(i.text)
        total = re.sub("\D", "", i.text)
        # total = filter(str.isdigit,  i.text)
    browser.delete_all_cookies()
    # test
    total = 2
    URL = 'https://sdasdasertre.xyz/forum-2-'
    for i in range(1, int(total)+1):
        print("now crawler page: "+str(i))
        url = URL + str(i) + '.html'
        search(word, url)
# url = 'https://www.zhongziso.com/'
wait = WebDriverWait(browser, 10)

def search(KEYWORD, URL):
    try:
        print(URL)
        browser.get(URL)
        '//*[@id="normalthread_524764"]/tr/th/a[2]'
        '#normalthread_524764 > tr > th > a.s.xst'
        '#threadlisttableid'
        # total = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#wrapp > div.jumbotron > div > div > ul:nth-child(4) > li:nth-child(8) > a")))
        #threadlisttableid
        '''#normalthread_524759 > tr > th'''
        # driver.find_element_by_css_selector('.s_ipt')
        # new = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.bm_c .new')))
        new = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'th > a.s.xst')))
        
        with open('Torrent.txt', 'a', encoding="utf-8") as f:
            for i in new:
                text=i.text + "\n"
                f.write(text)
                url = i.get_attribute('href').strip()
                f.write(url)
                print(text+"  "+url)
        # return total[0]
    except TimeoutException:
        return search

def Operate(url):
    try:
        browser.get(url)
    except TimeoutException:
        return Operate

def main2():
    KEYWORD = '电影'
    total = search(KEYWORD)
    print(total)
    newURL = 'https://www.zhongziso.com/list/'+ KEYWORD
    for i in range(1,int(total)):
        Operate(newURL+'/'+str(i))


if __name__ == '__main__':
    main()
    browser.delete_all_cookies()
    browser.close()
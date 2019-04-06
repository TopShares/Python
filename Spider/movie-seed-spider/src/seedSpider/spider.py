# -*- coding:utf-8 -*-
__author__ = 'RecXI'

from seedSpider.movie import Movie
import os
import re
import sys
import operator
import requests
from bs4 import BeautifulSoup as BS
import logging
from logging import info
from logging import debug
logging.basicConfig(level=logging.INFO)
import time
import threading



def seed_spider(category):
    
    # 首先获取总页码数
    url = "http://www.bttt.la/category.php?/" + category + "/1/"
    page = requests.get(url)
    soup = BS(page.text,"html.parser")
    print(soup)
    return
    page_num_info = soup.select("body > div.mb.cl > div.ml > ul > span")[0].text
    page_num = page_num_info.split("/")[0]
    reg = re.compile(r"\d+")
    page_num = reg.findall(page_num)[0]  # page_num存储总页数
    
    movie_list = []
    info("开始爬取类型：" + category + "\r\n")
    # 对页面进行解析：
    for page_num in range(1,int(page_num)):
        url = "http://www.bttt.la/category.php?/" + category + "/"+str(page_num)+"/"
        page = requests.get(url)
        soup = BS(page.text,"html.parser")
        
        # 获取每一部电影的名称，评分，下载链接
        for i in range(2,35):
            name = soup.select("body > div.mb.cl > div.ml > div:nth-of-type("+str(i)+") > div.title > p.tt.cl > a > b")     #片名
            if len(name) != 0:
                name = name[0].text.split(r"/")[0]
            score_1 = soup.select("body > div.mb.cl > div.ml > div:nth-of-type("+str(i)+") > div.title > p.rt > strong")    #评分的整数部分
            score_2 = soup.select("body > div.mb.cl > div.ml > div:nth-of-type("+str(i)+") > div.title > p.rt > em.fm")     #评分的小数部分
            href_element = soup.select("body > div.mb.cl > div.ml > div:nth-of-type("+str(i)+") > div.title > p.tt.cl > a") #链接

            # 对空白区域进行异常捕捉
            try:
                score = float(score_1[0].text+"."+score_2[0].text)
                href = "http://www.bttt.la/"+href_element[0]["href"]
                movie = Movie(name,score,href)      # 将影片信息封装成对象
                movie_list.append(movie)            # 用列表存放movie对象
            except:
                continue    
    
    # 按评分从高到低，对影片对象进行排序
    cmpfun = operator.attrgetter('score')
    movie_list.sort(key = cmpfun,reverse=True)
    count = 1
    
    # 将整理好的影片信息，分类别写入HTML文件中
    filename = category+"_种子.html"
    with open(filename,"wb") as f:
        for movie in movie_list:
            write_txt = r"<p>%s.&nbsp&nbsp&nbsp片名：%s&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp评分：%s&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp链接：<a href='%s' target='_blank'>%s</a></p>" % (str(count),movie.name,movie.score,movie.href,movie.href)
            f.write(write_txt.encode("utf-8"))
            count = count+1
    
    info(category + "类型  爬取结束\r\n")


# 主函数，多线程爬取：一个类型启用一个线程
def main(categories):
    thread_list = []
    cnt = len(categories)
    for category in categories:
        t = threading.Thread(target = seed_spider,args = (category,))
        thread_list.append(t)
    for t in thread_list:
        # t.setDaemon(True)
        t.start()
    for t in thread_list:
        t.join()
    print("全部爬取结束，快去收割种子吧！")
    # 脚本运行结束时，弹出文本文件以提示
    os.system(".\end.txt")
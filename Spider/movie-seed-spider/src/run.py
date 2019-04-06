# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup as BS
import requests
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

headers={
    "Host":"www.zhihu.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
    "Accept":"*/*",
    "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding":"gzip, deflate",
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With":"XMLHttpRequest",
    "Connection":"keep-alive"
}

category = '喜剧'
url = "https://www.bttt.la/category.php?/" + category
url = "https://www.banglong.site"
url = "https://www.bttt.la"
page = requests.get(url, headers=headers, verify=False)
soup = BS(page.text,"html.parser")
print(soup)
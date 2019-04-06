'''
read.douban.com
提取所有出版社
'''
import requests

Url =  'https://read.douban.com/provider/all'



headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2716.5 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
}

html = requests.get(Url, headers=headers)

import re

'''
<div class="name">浙江摄影出版社</div>
<div class="name">中国青年出版社</div>
<div class="name">中国民主法制出版社</div>
'''
pattern = '<div class="name">(.*?)</div>'
result = re.compile(pattern).findall(html.text)


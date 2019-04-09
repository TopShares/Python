
import requests
from lxml import etree
import urllib3  # 忽略https安全认证
urllib3.disable_warnings()
# SSR: https://github.com/shadowsocksrr/shadowsocksr-csharp/releases


#TODO
# url = 'https://www.mide.ml/tool/free_ssr'

# url = 'https://sphard2.github.io/gfw/free/ssr.html'
# url = 'https://github.com/shinelp100/ssr-free'
url = 'https://github.com/dxxzst/Free-SS-SSR'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}
response = requests.get(url, headers=headers, verify=False)
html = etree.HTML(response.content.decode())




import datetime
y = datetime.datetime.now().year
m = datetime.datetime.now().month
d = datetime.datetime.now().day
l = []
l.append(str(y))
l.append(str(m))
l.append(str(d))
now = '-'.join(l)

xpaths = '//*[@id="readme"]/div[2]/article/p[2]/text()'
old = html.xpath(xpaths)
old = str(old).split(" ")
old = str(old[0]).split("：")
# old[1]

n1 = datetime.datetime.strptime(now, "%Y-%m-%d")
n2 = datetime.datetime.strptime(old[1], "%Y-%m-%d")
print("page's time: " + old[1])

if n2 >= n1:
    print("正在写入...")
else:
    exit()
xpaths = '//*[@id="readme"]/div[2]/article/table/tbody//tr'

trs = html.xpath(xpaths)
li = []
for td in trs:
    txt = td.xpath('.//td/text()')
    li.append(txt[1])
with open('SSR.txt','w') as f:
    for i in li:
        f.write(i + '\n')
print('./SSR.txt')
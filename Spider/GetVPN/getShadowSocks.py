
import requests
from lxml import etree
import urllib3  # 忽略https安全认证
urllib3.disable_warnings()

url = 'https://sphard2.github.io/gfw/free/ssr.html'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}
response = requests.get(url, headers=headers, verify=False)
html = etree.HTML(response.content.decode())
# parser = etree.HTMLParser(encoding='utf-8')
# html = etree.parse(response.text, parser=parser)


import datetime
y = datetime.datetime.now().year
m = datetime.datetime.now().month
d = datetime.datetime.now().day
l = []
l.append(str(y))
l.append(str(m))
l.append(str(d))
now = '-'.join(l)

ele = html.xpath('///*[@id="book-search-results"]/div[1]/section/h4/text()')
e = str(ele[0]).split("日")

# n2 = '2019年3月9'
old = e[0].replace('年','-')
old = old.replace('月','-')


n1 = datetime.datetime.strptime(now, "%Y-%m-%d")
n2 = datetime.datetime.strptime(old, "%Y-%m-%d")
print("page's time: " + old)

if n2 >= n1:
    print("正在写入...")
else:
    exit()

trs = html.xpath('//*[@id="book-search-results"]/div[1]/section/table[1]/tbody//tr')
myDic = {
    'IP':'server',
    '端口':'server_port',
    '密码':'password',
    '加密':'method',
    '协议':'protocol',
    '混淆':'obfs',
}
dic = {}
for td in trs:
    txt = td.xpath('.//td/text()')
    if txt[0] in myDic:
        txt[0] = myDic[txt[0]]
    for index, item in enumerate(txt):
        if index % 2 ==0:
            dic[item] = txt[index+1]
import json
li = []
li.append(dic)
with open('./ssr.json','w') as f:
    ssr = {
        "configs": li
    }
    f.write(json.dumps(ssr))
print("写入成功")
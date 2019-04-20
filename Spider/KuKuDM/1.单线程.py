import time
import re
import os
import requests
from lxml import etree

class Crawler:
	def __init__(self, data):
		self.datas = data
		self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0',' WOW64) AppleWebKit/537.cipg (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"}
    
	def run(self):
		self.getPicUrlList()
			

	def getPicUrlList(self):
		for i in self.datas:
			html = self.getHTMLText(i['url'])

			pattern = re.compile('上一页</li><li>([\s\S]*?)</li>')
			allPage = re.findall(pattern, html)
			allPage = (allPage[0]).split('/')[1]

			for url_i in range(1, int(allPage)+1):
				url = re.sub(r'(\d+)(?=.htm)', str(url_i), i['url'])
				# print(url)	#https://m.kukukkk.com/comiclist/2286/70563/13.htm
				html = self.getHTMLText(url)

				pattern = re.compile("IMG SRC='([\s\S]*?)'")
				imgUrl = re.findall(pattern, html)
				imgUrl = imgUrl[0].replace('''"''', "").replace("+", "")

				parameter_global_js = ({
				# "server0": "http://n.1whour.com/",
				# "server": "http://n.1whour.com/",
				# "m200911d": "http://n.1whour.com/",
				# "m201001d": "http://n.1whour.com/",
				'm2007':'http://m8.1whour.com/',
				})
				for _i in parameter_global_js:
					urlPic = imgUrl.replace(str(_i), str(parameter_global_js[_i]))
					self.SavePic(urlPic, i['txt'])

	def SavePic(self, picUrl, folderPath):
		headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0',' WOW64) AppleWebKit/537.cipg (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"}
		folder = picUrl.split('/')[-1:]
		folder = folderPath + '/' + folder[0]
		isExists = os.path.exists(folderPath)
		if not isExists:  # 目录不存在，则创建
			os.makedirs(folderPath)

		r = requests.get(picUrl,headers=headers)

		with open(folder, 'wb') as f:
			f.write(r.content)

	def getHTMLText(self, url):
		try:
			r = requests.get(url, headers=self.headers)
			r.raise_for_status()
			if r.status_code == 200:  # ok
				return r.content.decode('gbk') 
			else:
				return None
		except:
			return None



def getUrlList(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0',' WOW64) AppleWebKit/537.cipg (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"}
    html = ''
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        if r.status_code == 200:  # ok
            html = r.content.decode('gbk') 
        else:
            return None
    except:
        return None

    html = etree.HTML(html)
    folder = html.xpath('//*[@id="comicName"]/text()')
    folder = './' + folder[0]
    isExists = os.path.exists(folder)
    if not isExists:  # 目录不存在，则创建
        os.makedirs(folder)
    e = html.xpath('//*[@class="classBox autoHeight"]/div/li//a')
    data = []
    tmp = {}
    index = 1
    for i in e:
        tmp['url'] = 'https://m.kukukkk.com' + i.xpath('./@href')[0]
        tmp['txt'] = folder + '/' + str(index).zfill(2) + '.'+ i.xpath('./text()')[0]
        data.append(tmp)
        tmp = {}
        index += 1
    return data


def test():
    url = 'https://m.kukukkk.com/comiclist/2286/'
    data = getUrlList(url)
    c = Crawler(data)
    c.run()
    print('OK')


if __name__=='__main__':
    start = time.time()
    test()
    end = time.time()
    print("Finished in Time Consuming: {}".format(end-start))
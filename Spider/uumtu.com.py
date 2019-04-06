import os
import re
from urllib.request import urlretrieve
import requests
import concurrent.futures  # Python3.2+ 线程池模块

def downloadImg(folderPath, imgUrl, file=''):
    folderPath = str(folderPath).replace('.', '')
    folderPath = folderPath.replace(':', '')

    if file is None:
        imgeNameFromUrl = os.path.basename(imgUrl)
        imgName = imgeNameFromUrl
    else:
        imgName = file
    filename = folderPath + "\\" + str(imgName)

    if os.path.exists(filename) is True:
        return False

    # ------ 异常处理 ------
    try:
        # imgContent = (urllib.request.urlopen(imgUrl)).read()
        r = requests.get(imgUrl, stream=True, timeout=500)
        imgContent = r.content
    except urllib.error.URLError as e:
        print('【错误】无法下载')
        return False
    except:
        return False
    else:


        # ------ IO处理 ------
        isExists = os.path.exists(folderPath)
        try:
            if not isExists:  # 目录不存在，则创建
                os.makedirs(folderPath)
        except:
            pass
        try:
            print(filename)
            with open(filename, 'wb') as f:
                f.write(imgContent)  # 写入本地磁盘
            sum += 1
        except:
            return False
        return True


thePoolSize = 5
def Go(data):
    print(data)
    futures = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=thePoolSize) as pool:
        for index in data:
            torrentURL = index[0]
            filename = index[1]
            futures.append(pool.submit(downloadImg, PATH, torrentURL, filename))

def getImg(image_url):
	html = requests.get(image_url)
	rep = re.compile(r'<img src="(.*?)" alt="(.*?)" />')
	result = re.findall(rep, html.text)
	return result

if __name__ == '__main__':
	PATH= 'data'
	if not os.path.isdir("./data"):
	    os.mkdir("data")
	model = 'https://www.uumtu.com/mote/wangyuchun.html'

	URL = 'https://www.uumtu.com/siwa/'
	image_url = "https://www.uumtu.com/siwa/28470.html"
	#page one
	urlList = []
	urlList.append(getImg(image_url))

	html = requests.get(image_url)
	rep = re.compile(r'href="/siwa/(.*?).html">末页')
	result = re.findall(rep, html.text)
	total = (((((result[0]).split('/'))[-1:])[0]).split('_'))
	typeNum = total[0]
	total = total[-1:][0]
	go = 2
	for go in range(go, int(total) + 1):
		tmp = URL + typeNum + '_' + str(go) + '.html'
		tmp = getImg(tmp)
		urlList.append(tmp)
	Go(urlList)

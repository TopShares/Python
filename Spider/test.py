import re
# https://www.uumtu.com/28470_34.html
url = 'http://www.2.com/1.htm'
allPage = 10
picUrlList= []


for url_i in range(1, int(allPage)+1):
    url = re.sub(r'(\d+)(?=.htm)', str(url_i), url)
    picUrlList.append(url)
print(picUrlList)

picUrlList = [re.sub(r'(\d+)(?=.htm)', str(e), url) for e in range(1,allPage)]
print(picUrlList)
a = ['https://m.kukukkk.com_'+str(x) for x in range(5)]
# print(a)
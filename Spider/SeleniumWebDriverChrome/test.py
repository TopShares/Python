
import urllib.parse

url =r'https://wer.com/i733/8734.html?sid=23833' 
url, frag = urllib.parse.urldefrag(url)
res=urllib.parse.urlsplit(url)
print(res.scheme)
print(res.netloc)
print(res.path)

print('*'*99)

baseUrl = 'https://manhua.fzdm.com/56/'  

path = r'311/'

test = urllib.parse.urljoin(baseUrl,path)
print(test)


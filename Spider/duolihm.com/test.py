url = 'https://www.duolihm.com/book/607'
from urllib.parse import urlsplit

result = urlsplit(url)
"""
(scheme='https'（协议）, netloc='www.duolihm.com'（域）, 
path='/daxuesheng'（路径）, params=''（可选参数）, 
query='name=zhangsan'（查询参数）, fragment='123'（锚点）)
"""

print(result.scheme+"//" + result.netloc )


# print(urljoin('http://www.cwi.nl/%7Eguido/Python.html', 'FAQ.html'))
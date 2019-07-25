#使用代理：
EG_1:

conn = aiohttp.ProxyConnector(proxy="http://some.proxy.com")----创建代理
session = aiohttp.ClientSession(connector=conn)
async with session.get('http://python.org') as resp:
print(resp.status)

# EG_2:
conn = aiohttp.ProxyConnector(
	proxy="http://some.proxy.com",
	proxy_auth=aiohttp.BasicAuth('user', 'pass')
)

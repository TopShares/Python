import asyncio


@asyncio.coroutine
def fetch_async(host, url='/'):
    print(host, url)
    reader, writer = yield from asyncio.open_connection(host, 80)

    request_header_content = """GET %s HTTP/1.0\r\nHost: %s\r\n\r\n""" % (url, host,)
    request_header_content = bytes(request_header_content, encoding='utf-8')

    writer.write(request_header_content)
    yield from writer.drain()
    text = yield from reader.read()
    print(host, url, text)
    writer.close()

tasks = [
    fetch_async('www.cnblogs.com', '/wupeiqi/'),
    fetch_async('dig.chouti.com', '/pic/show?nid=4073644713430508&lid=10273091')
]

loop = asyncio.get_event_loop()
results = loop.run_until_complete(asyncio.gather(*tasks))
loop.close()
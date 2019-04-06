from twisted.web.client import getPage, defer
from twisted.internet import reactor

def all_done(arg):
    reactor.stop()


def callback(contents):
    print(contents)


deferred_list = []

url_list = ['http://www.bing.com', 'http://www.baidu.com', ]
for url in url_list:
    deferred = getPage(bytes(url, encoding='utf8'))
    deferred.addCallback(callback)
    deferred_list.append(deferred)

dlist = defer.DeferredList(deferred_list)
dlist.addBoth(all_done)

reactor.run()

#Twisted示例
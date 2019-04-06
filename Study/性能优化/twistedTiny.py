#!/usr/bin/env python
# -*- coding:utf-8 -*-
from twisted.web.client import getPage
from twisted.internet import reactor
from twisted.internet import defer


@defer.inlineCallbacks
def task(url):
    ret = getPage(bytes(url, encoding='utf8'))
    ret.addCallback(callback)
    yield ret


def callback(arg):
    print('回来一个', arg)


url_list = ['http://www.bing.com', 'http://www.baidu.com', ]
defer_list = []
for url in url_list:
    ret = task(url)
    defer_list.append(ret)


def stop(arg):
    print('已经全部现在完毕', arg)
    reactor.stop()


d = defer.DeferredList(defer_list)
d.addBoth(stop)
reactor.run()

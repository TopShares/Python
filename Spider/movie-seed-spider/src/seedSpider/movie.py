'''
影片类：封装影片相关信息
包括：片名，评分，下载链接
'''

class Movie(object):
    def __init__(self,name,score,href):
        self.name = name
        self.score = score
        self.href = href
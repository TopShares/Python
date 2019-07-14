# -*- coding: utf-8 -*-
import requests
import time
import sys

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.host = "http://api.jima123.com/api.php?act=login"

    def doLogin(self):
        url_params = {
            'username': self.username,
            'password': self.password,
            'developer': 'jfTuA2ZFz4mnxRChtJfyk4cHk2XPZvP9',
        }
        data = returnJsonData(self.host, url_params)
        self.userID = data[0]['userid']
        self.token = data[0]['token']
        return True

    def getUserInfo(self):
        if self.doLogin():
            url = r'http://api.jima123.com/api.php?act=getinfo'
            url_params = {
                'userid': self.userID,
                'token': self.token
            }
            data = returnJsonData(url, url_params)
            print(data)
    def getTask(self):
        if self.doLogin():
            url = r'http://api.jima123.com/api.php?act=gettask'
            url_params = {
                'userid': self.userID,
                'token': self.token
            }
            data = returnJsonData(url,url_params)
            # 查询 拼多多
            for i in range(len(data)):
                if data[i]['taskname'] == '拼多多':
                    self.taskid = data[i]['taskid']
                    return True
        return False

    def getMobile(self):
        if self.getTask():
            url = r'http://api.jima123.com/api.php?act=getmobile'
            url_params = {
                'userid': self.userID,
                'token': self.token,
                'taskid': self.taskid,
                # 参数名     必选   缺省值	    说明
                # count	否	1	获取数量[缺省默认为1]
                # area	否		地区[不填则 随机]
                # operator 否		运营商 [不填为 0] 0 [随机] 1 [移动] 2 [联通] 3 [电信]
                # mobile	否		获取指定的手机号
                # key	否		专属对接，与卡商直接对接
            }
            data = returnJsonData(url,url_params)
            self.mobile = data[0]['mobile']
            return True
        return False

    def getSMS(self):
        if self.getMobile():
            url = r'http://api.jima123.com/api.php?act=getsms'
            url_params = {
                'userid': self.userID,
                'token': self.token,
                'taskid': self.taskid,
                'mobile': self.mobile,
            }
            r = requests.post(url=url, params=url_params)
            data = r.json()
            while data['sms'] == "":
                print(self.mobile)
                r = requests.post(url=url, params=url_params)
                data = r.json()
                print(data)
                time.sleep(15)
        self.quitToken()

    def quitToken(self):
        url = r'http://api.jima123.com/api.php?act=quit'
        url_params = {
            'userid': self.userID,
            'token': self.token,
        }
        r = requests.post(url=url, params=url_params)
        data = r.json()
        if data['errno'] == "0":
            print("Quit Token Success")

def returnJsonData(url, url_params):
    r = requests.post(url=url, params=url_params)
    data = r.json()
    if data['errno'] is '0':
        return data['data']
    return False

if len(sys.argv) != 3:
    print("USAGE: python3 jima.py <用户名> <密码>")
    sys.exit(1)
USERNAME = sys.argv[1]
PASSWORD = sys.argv[2]

if __name__ == '__main__':
    user = User(USERNAME, PASSWORD)
    user.getUserInfo()
    user.getSMS()
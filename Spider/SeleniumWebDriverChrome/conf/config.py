from conf.db import MongoDB
import os

class config:
    mongodb = None
    browser = None

    def __init__(self):
        self.db_conf(self)
        self.selenium_conf(self)

    def db_conf(self, uri='mongodb://localhost:27017/', db='test', collection='test'):
        # 常量定义
        uri = "mongodb://localhost:27017/"
        db = "MyDB"
        collection = "test"
        self.mongodb = MongoDB(uri, db, collection)  # 连接数据库

    
    def selenium_conf(self, headless=True):
        from selenium.webdriver import ChromeOptions
        option = ChromeOptions()
        if headless:
            option.add_argument('--headless')

        from selenium import webdriver
        abspath = os.path.abspath(r"C:\Program Files\Google\Chrome\Application\chromedriver.exe")
        self.browser = webdriver.Chrome(abspath, options=option)


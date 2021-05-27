from conf.db import MongoDB
import os


class config:
    mongodb = None
    browser = None
    mongodbURI = 'mongodb://localhost:27017/'
    mongoDB = 'test'
    mongoCollection = 'test'

    def __init__(self):
        self.db_conf(self.mongodbURI, self.mongoDB, self.mongoCollection)
        self.selenium_conf(self)

    def db_conf(self, uri, db, collection):
        # 常量定义
        self.mongodb = MongoDB(uri, db, collection)  # 连接数据库

    def selenium_conf(self, headless=True):
        from selenium.webdriver import ChromeOptions
        option = ChromeOptions()
        if headless:
            option.add_argument('--headless')

        from selenium import webdriver
        abspath = os.path.abspath(
            r"C:\Program Files\Google\Chrome\Application\chromedriver.exe")
        self.browser = webdriver.Chrome(abspath, options=option)

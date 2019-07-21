from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time,os
# 参数对象， 控制Chrome以无界面模式打开
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

abspath = os.path.abspath(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe") 
# 创建浏览器对象
browser = webdriver.Chrome(executable_path=abspath,chrome_options=chrome_options)

url = 'http://www.baidu.com'
browser.get(url)
# time.sleep(3)
browser.save_screenshot('baidu.png')

#
browser.quit()
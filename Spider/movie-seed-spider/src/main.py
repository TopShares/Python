'''
脚本启动模块
'''

import seedSpider.spider as s

print("\r\n请正确输入你想爬取的电影_电视剧类型,可输入类型包括：\r\n")
print("动作 战争 剧情 爱情 科幻 悬疑 家庭 犯罪 恐怖 动画 喜剧 惊悚 冒险 电视剧\r\n")
categories = input("如果需要一次爬取多个类型，不同类型中间请用空格隔开：\r\n")
categories = categories.split()
s.main(categories)
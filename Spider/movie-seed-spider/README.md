# movie-seed-spider
# 电影种子爬虫
*同时解决片荒，烂片筛选两个难题*
## python版本
3.6.1 :: Anaconda 4.4.0 (64-bit)

## 主要功能
**1. 分类别爬取BT天堂的电影下载链接，每个类别启用一个线程**

**2. 按电影评分从高到低进行排序，避免烂片**

![screeshots_1](https://github.com/RecXI/movie-seed-spider/blob/master/screenshots/1.png)

**3. 使用者可以根据喜好输入自己想要爬取的类型**

![screeshots_2](https://github.com/RecXI/movie-seed-spider/blob/master/screenshots/2.png)

**4. 爬取结果以HTML文件存储，方便跳转至下载链接**

![screeshots_3](https://github.com/RecXI/movie-seed-spider/blob/master/screenshots/3.png)

5. 爬取需要花费一定时间，但是爬取结束时会自动弹出文本文件提示结束。所以爬取过程可以尽情去做其他事情，不用随时查看脚本运行情况

![screeshots_4](https://github.com/RecXI/movie-seed-spider/blob/master/screenshots/4.png)

## 使用方法
保持源码目录结构，打开命令行终端，cd到main.py所在目录，然后键入命令：

`python main.py`

根据字符信息提示，输入你想要爬取的类型，并以空格隔开。

爬取结束后会自动弹出文本文件提示结束,之后便可以查阅在目录下生成的HTML文件。

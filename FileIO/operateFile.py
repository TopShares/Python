import os
import re
from MyFunFile import *
# from MyFunFile import getNumber, getTen

def openPath(path=""):
    fileList = os.listdir(path)   #获取path目录下所有文件
    for filename in fileList:
        pathTmp = os.path.join(path,filename)   #获取path与filename组合后的路径
        if os.path.isdir(pathTmp):   #如果是目录
            # pass
            openPath(pathTmp)        #则递归查找
            '''
            目录更名
            '''
            # print(filename)
            # out = rmAD(filename)
            # out = getNumber(filename)  # 中文数字转英文
            # newPath = os.path.join(path,str(out))
            # os.renames(pathTmp,newPath)

        else: # 文件
            # pass
            # print("file: "+ pathTmp)
            # print("name: "+filename)
            # exten = os.path.splitext(filename)   # 取文件 后缀
            # if exten[1] == '.txt':
            #     new = exten[0]
            # new = re.sub('_52studyit.com', '', filename)        # sub
            # new = rmAD(filename)              # 删除【】广告
            # new = addNum(filename)            # 个位数字后加点
            # new = addDot(filename)            # 数字后加点
            new = getNumber(filename)         # 中文转阿拉伯数字
            newPath = os.path.join(path, new)
            os.renames(pathTmp,newPath)

def main():
    path = r''
    p=r'E:\MYSQL数据库底层封装教程'
    p=r'C:\Users\Administrator\Desktop\新建文件夹 (2)'
    openPath(p)


if __name__ == '__main__':
    main()

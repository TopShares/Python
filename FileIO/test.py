import os
import re
from MyFunFile import *
# from MyFunFile import getNumber, getTen
 
def openPath(path=""):
    fileList = os.listdir(path)   #获取path目录下所有文件
    n=0   
    for filename in fileList:
        pathTmp = os.path.join(path,filename)   #获取path与filename组合后的路径
        if os.path.isdir(pathTmp):   #如果是目录
            # openPath(pathTmp)        #则递归查找

            '''
            目录更名
            '''
            #设置新文件名
            s=str(n+1)
            st=s.zfill(5)   #这里的数字为名称的总数位，比如000000递增就是6
            newname= st+ filename
            # print(filename)
            # print(newname)
            # out = getNumber(filename)
            newPath = os.path.join(path,newname)
            print(newPath)
            os.renames(pathTmp,newPath)
        n+=1

def main():
    path = r'C:\Users\1\Desktop\GitHub\infoCrawler\Datas'
    openPath(path)


if __name__ == '__main__':
    main()
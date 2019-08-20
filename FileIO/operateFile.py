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
            print(filename)
            # out = rmAD(filename)
            out = __getNum(filename)  # 中文数字转英文
            newPath = os.path.join(path,str(out))
            os.renames(pathTmp,newPath)
            # out = getTen(pathTmp[-1:])
        #     if out is not 10:
        #         newPath = os.path.join(path,str(out))
        #         os.renames(pathTmp,newPath)
        #     print(pathTmp)

        else: # 文件
            # pass
            # print("file: "+ pathTmp)
            # print("name: "+filename)
            # exten = os.path.splitext(filename)   # 取文件 后缀
            # if exten[1] == '.txt':
            #     new = exten[0]
            #     newPath = os.path.join(path, new)
            #     # print(pathTmp,newPath)
            #     os.renames(pathTmp,newPath)
            # new = getNumber(filename)
            # new = addNum(filename)      # 个位数字后加点
            new = addDot(filename)          # 数字后加点
            # new = rmAD(filename)
            newPath = os.path.join(path, new)
            os.renames(pathTmp,newPath)
            # print(newPath)
            # print("new"+new)
            # # new = re.sub('_recv','',filename)
            # newPath = os.path.join(path, new)
            # os.renames(pathTmp,newPath)

            '''
            # out = rmAD(filename)
            out = getNumber(filename)
            print(out)
            if out is not None:
                newPath = os.path.join(path,out)
                os.renames(pathTmp,newPath)

            # newPath = os.path.join(path, rmAD(filename))
            # os.renames(filename,newPath)
            '''

def main():
    # path=r"C:\Users\Pancras\Desktop\课件" 
    # lis = [s+str(i) for i in range(2,52)]
    # for path in lis:
    #     openPath(path)
    # path = r'F:\多啦A梦[xxxx.xxx]'
    # path = r'E:\21 git安装和使用'
    path = r'E:\08. 超全技术电子书汇总'
    path = r'E:\玩转算法与数据结构'
    openPath(path)


if __name__ == '__main__':
    main()

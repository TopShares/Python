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
            # # print(filename)
            # newPath = os.path.join(path,str(out))
            # print("old: "+pathTmp)
            # print("new: "+newPath)
            # os.renames(pathTmp,newPath)
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
            new = rmAD(filename)            # 删除【】广告
            # new = addNum(filename)      # 个位数字后加点
            # new = addDot(filename)          # 数字后加点
            # new = rmAD(filename)
            newPath = os.path.join(path, new)
            os.renames(pathTmp,newPath)
            # print(newPath)
            # print("new"+new)
            # # new = re.sub('_recv','',filename)
            # newPath = os.path.join(path, new)
            # os.renames(pathTmp,newPath)

            '''
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
    path = r''
    path = r'E:\10_Vue【北京尚学堂·百战程序员】\05_Vue实战练习【北京尚学堂·百战程序员】'
    path = r'E:\微专业 - 数据可视化（价值2200元）'
    path = r'E:\蓝桥杯国赛训练营（19年）'
    path = r'E:\【瑞客论坛 www.ruike1.com】蓝桥杯 - 数据结构不难（19年）'
    path=r'E:\【瑞客论坛 www.ruike1.com】零基础英语首发班（已完结）'
    openPath(path)


if __name__ == '__main__':
    main()

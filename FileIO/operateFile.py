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
            # new = addDot(filename)          # 数字后加点
            new = rmAD(filename)				#  删除【】广告
            newPath = os.path.join(path, new)
            os.renames(pathTmp,newPath)
            # print(newPath)
            # print("new"+new)
            # # new = re.sub('_recv','',filename)
            # newPath = os.path.join(path, new)
            # os.renames(pathTmp,newPath)

def main():
    # path=r"C:\Users\Pancras\Desktop\课件"
    # lis = [s+str(i) for i in range(2,52)]
    # for path in lis:
    #     openPath(path)
    path = r'E:\Java'
    path=r'E:\【瑞客论坛 www.ruike1.com】CTF夺旗训练视频课程'
    path=r'E:\【瑞客论坛 www.ruike1.com】百知教育 - 面向对象的基础'
    path=r'E:\【瑞客论坛 www.ruike1.com】2020年最新 深圳Java190722班技术简历辅导'
    path=r'E:\【瑞客论坛 www.ruike1.com】【天勤】2021天勤计算机全程班【现售：￥1980】'
    path=r'E:\【瑞客论坛 www.ruike1.com】黑马头条项目 - Java Springboot2.0（资料、代码。讲义）14天完整'
    path=r'E:\【瑞客论坛 www.ruike1.com】spring源码底层分析'
    openPath(path)


if __name__ == '__main__':
    main()

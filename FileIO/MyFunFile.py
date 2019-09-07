import re
num=['零','一','二','三','四','五','六','七','八','九']
key = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
k=['十','百','千','万']


def __getNum(string):
    '''
    百位内转换
    '''
    lszie = len(string)
    result = ''
    ten = ''
    count = 0
    tmp = ''
    for i in string:
        count += 1
        if i in num:
            #个位
            if lszie == 1:
                result = '0' + str(num.index(i))
            else:
                result = str(num.index(i))
        elif i == '十':
            if lszie > 1:
                tmp = ''
            if lszie == 2 and count == 1:
                ten = '1'
                result = ten + result
            elif lszie == 1:
                result = '10'
            elif count == lszie:
                tmp = ''
                ten = '0'
                result = result + ten
        tmp += result
    return tmp
# print(__getNum('九十九'))

def getNumber(string):
    '''
    将中文的数字改成纯数字
    '''
    Num = re.findall(r'第(.*?)[课|讲|节|章|周|天]', string, re.S) # 中文数字
    if Num:
        Num = __getNum(Num[0])    # 转换成数字
    out = re.sub(r'[^?=第].*(?=课|讲|节|章|周|天)', str(Num), string)
    return out
# print(getNumber('第十课_自动摘要及正文抽取'))
# print(getNumber('第二十九讲（漫画作文）【公众号】免费分享'))

def rmAD(str):
    '''
    删除【】广告
    :param str
    :return: str
    '''
    pattern = re.compile(r'【(.*?)】')
    out = pattern.sub('', str)
    return out

# a = rmAD('25_3_选择排序【溜须拍马顺】')
# print(a)

def rmAD2(str):
    '''
    删除含[]的广告
    :param str
    :return: str
    '''
    pattern = re.compile(r'\[([^\[\]]*)\]') #匹配含[]内容
    out = pattern.sub('', str)
    return out
# a = rmVxia('F:\多啦A梦[this test]')
# print(a)

def addNum(str):
    '''
    一位数字前面加个零
    :param str
    :return: str
    '''
    num = re.findall(r'(^\d)[^\d]', str)
    if num:
        out = re.sub(r'(^\d)[^\d]', '0'+num[0]+'.', str)
        return out
    else:
        return str
# print(addNum('1.洛必达断点定义.mp4'))



def addDot(str):
    '''
    数字开头后加上点
    '''

    num = re.findall(r'(^\d{1,2})', str)
    if num:
        out = re.sub(r'(^\d{1,2})',num[0] + '.', str)
        return out
    else:
        return str

# addDot(r'1response网络详细信息.mp4')

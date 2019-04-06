import re


# 匹配.com和.cn网址
string =  '''<a href="http://www.163.com.cn">网易</a> '''
pattern = "[a-zA-Z]+://[^\s]*[.com|.cn]"
result = re.compile(pattern).findall(string)
print(result)

# 匹配phone number
pattern = "\d{11}"
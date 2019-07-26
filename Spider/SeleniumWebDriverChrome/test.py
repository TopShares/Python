import jsonpath,json 
 
with open('data.json', 'r', encoding='utf-8')as f:

    # 把json格式字符串转换成python对象
    jsonobj = json.load(f)\
 
# res = html.xpath('//*[@id="content"]//li//a')
# 从根节点开始，匹配name节点
txt = jsonpath.jsonpath(jsonobj,'$..txt')
url = jsonpath.jsonpath(jsonobj,'$..url')

print(txt,url)

print(type(txt))
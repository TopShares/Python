lis = [a + b for a in '123' for b in 'abc']

print(lis)

dic = {'k1':'v1', 'k2':'v2'}
a = [k+":"+v for k,v in dic.items()]

print(a)
dic = {i:i**3 for i in range(5)}
print(dic)


res = [lambda x:x + i for i in range(10)]
print(res[0](10))
print(res)
# [lambda x:x+i, ]
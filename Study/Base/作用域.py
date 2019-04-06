'''
L (Local)
E (Enclosing) 闭包函数外的函数中
G (Global)
B (Built-in)

global, nonlocal 半包外函数变量
'''

#例子
name = 'jack'
def f1():
    print(name)

def f2():
    name = 'eric'
    f1() # not print(name)
f2()

'''
print: jack
'''



#例2
name = 'jack'
def f22():
    name = 'eric'
    return f1
def f11():
    print(name)

ret = f22() # ret = f11()
ret() # -> f11()

'''
print: jack
'''
#coding:utf-8
'''
Created on 2016��6��7��

@author: Administrator
'''
#导入精确除法 1/2 = 0.5   而不是0
# from __future__ import division
# 
# def arithmetic(x=1,y=1,operator='+'):
#     result = {
#               '+':x+y,
#               '-':x-y,
#               '*':x*y,
#               '/':x/y
#               }
#     return result.get(operator)
# 
# print(arithmetic(1, 5))
# print(arithmetic(x=2, y=3, operator='+'))
# print(arithmetic( y=2))

#'*'可以引用元组，把多个参数组合到一起
def functi(* args):
    print(args)
    
functi(1,2,3)

#在形参面前添加‘**’，可以引用一个字典
def search(*t,**d):
    keys = d.keys()
    values = d.values()
    print(keys)
    print(values)
    for arg in t:
        for key in keys:
            if arg == key:
                print("find:",d[key])
search('one','three',one='1',two='2',three='3')

#没有return语句返回None
def funct():
    pass
print(funct())

#return 范湖多个值
def multFunc(x,y,z):
    l = [x,y,z]
    l.reverse()
    numbers = tuple(l)
    return numbers

x,y,z = multFunc(0, 1, 2)
print(x,y,z)
#匿名函数
print(reduce(lambda x,y:x*y, range(1,5)))

def funcGe(n):
    for i in range(n):
        print(i)
        yield i

for i in funcGe(3):
    print('hehe:-->',i)

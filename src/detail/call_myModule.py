#coding:utf-8
'''
Created on 2016年6月6日
@author: Administrator
'''
def sum(x=1,y=2):
    return x + y

print(sum(1, 3))


def say():
    print('say in')

apply(say)

print(apply(sum,(1,5)))

def func(x):
    if x>0:
        return x

#filter 过滤函数
print(filter(func, range(-9,10)))





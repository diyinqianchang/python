#coding:utf-8
'''
Created on 2016年6月6日
@author: Administrator
'''
from __builtin__ import apply
def sum(x=1,y=2):
    return x + y

print(sum(1, 3))


def say():
    print('say in')

apply(say)
print(apply(sum,(1,5)))
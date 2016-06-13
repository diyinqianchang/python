#coding:utf-8
'''
Created on 2016��6��13��
__new__()在__init__()之前被调用，用于生成实例对象。利用这个方法和类属性的特性可以
以实现设计模式中的单利模式。单例模式设计的类只能实例化一个对象
@author: Administrator
'''

class Singleton(object):
    '''
    单利
    '''
    __instance = None  #私有的类属性
    def __init__(self):
        pass
    def __new__(self, *args, **kwargs):
        if Singleton.__instance is None:
            Singleton.__instance = object.__new__(self, *args, **kwargs)
        return Singleton.__instance
        
        
if __name__ == '__main__':
    single1 = Singleton()
    single2 = Singleton()
    print(single1,single2)
    
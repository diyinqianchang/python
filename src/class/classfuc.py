#coding:utf-8
'''
Created on 2016��6��13��

@author: Administrator
'''

class MyClass(object):
    
    class Growth:
        def __call__(self):  #把实例对象当做函数返回
            print('grow....')
    grow = Growth()
    
    
    def __init__(self, color='red',price=0):
        self.__color = color
        self.__price = price
    
    def __getattribute__(self, name):
        return object.__getattribute__(self, name)
    
    def __setattr__(self, name, value):
        self.__dict__[name] = value

if __name__ == '__main__':
    fruit = MyClass('blue',10)
    print(fruit.__dict__.get('_MyClass__color'))
    fruit.__dict__['_MyClass__price'] = 5
    print(fruit.__dict__.get('_MyClass__price'))
    fruit.grow()
     
        
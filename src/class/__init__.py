#coding:utf-8
'''
Created on 2016年6月12号
@author: 张国林
'''
class Fruit:
    price = 0           #类属性
    
    def __init__(self):
        self.__color = 'red'    #实例属性
        zone = "China"    #局部变量
        self.__weight = 120    #私有属性 instance._classname__attribute
        
    def getColor(self):
        return self.__color
    
    @ staticmethod
    def getPrice():      #没有self参数
        return Fruit.price
    
#     def ggetPrice():
#         Fruit.price = Fruit.price+20
#         return Fruit.price
#     count = staticmethod(ggetPrice)    #staticmethod装换为静态方法
     
#Python的类和对象都可以访问类属性，而java中的静态变量只能被类调用   
if __name__ == '__main__':
    print(Fruit.price)
    apple = Fruit()
    print(apple.getColor())
    print(apple._Fruit__weight)
    Fruit.price = Fruit.price+10
    print(apple.price)
    banana = Fruit()
    print(banana.price)
    print(apple.__dict__)
    print(apple.__doc__)
    
    print(Fruit.getPrice())
#     print(Fruit.count())
    
    
    
    
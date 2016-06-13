#coding:utf-8
'''
Created on 2016年6月13日

@author: Administrator
'''
import gc
class Fruit:
    def __init__(self,name,color):
        self.__name = name;
        self.__color = color;

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    def getColor(self):
        return self.__color;
    def setColor(self,color):
        self.__color = color

class FruitShop:
    def __init__(self):
        self.fruit = []
    def addFruit(self,fruit):
        fruit.parent = self          #把Fruit关联FruitShop类
        self.fruit.append(fruit)
        
if __name__ == '__main__':
    shop = FruitShop()
    shop.addFruit(Fruit('apple','red'))
    shop.addFruit(Fruit('banana','yellow'))
    print(gc.get_referrers(shop))  #列出shop对象关联的所有对象
    del shop
    print(gc.collect())
          
    
        
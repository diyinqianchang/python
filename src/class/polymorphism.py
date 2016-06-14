#coding:utf-8
'''
Created on 2016��6��14��
@author: Administrator
'''
class Fruit(object):
    '''
    多态
    '''
    def __init__(self, color):
        self.color = color
class Apple(Fruit):
    def __init__(self,color='red'):
        Fruit.__init__(self, color)
class Banana(Fruit):
    def __init__(self,color='yellow'):
        Fruit.__init__(self, color)
        
class FruitShop(object):
    def sellFruit(self,fruit):
        if isinstance(fruit, Apple):
            print('sell apple')
        elif isinstance(fruit, Banana):
            print('sell banana')
        else:
            print('sell unkonwn fruit')
            
            
if __name__ == '__main__':
    shop = FruitShop()
    apple = Apple('red')
    banana = Banana()
    shop.sellFruit(apple)
    shop.sellFruit(banana)     
        
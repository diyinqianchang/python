#coding:utf-8

'''
Created on 2016年6月14日

@author: Administrator
'''

class Fruit(object):
    '''
    继承
    '''
    def __init__(self, color):
        self.color = color
        print("fruit's color : %s"% self.color)
    def grow(self):
        print('grow....')

class Apple(Fruit):
    def __init__(self,color):
        super(Apple,self).__init__(color)  #super 调用父类的方法。注意参数
        #super(type,obj) type是类 obj是类的实例
#         Fruit.__init__(self, color) #调用父类的方法
        print("apple's color %s"% self.color)
        
class Banana(Fruit):
    def __init__(self,color):
        Fruit.__init__(self, color)
        print("banana's color %s"% self.color)
    def grow(self):   #重写父类的方法
        print('banana grow....')


if __name__ == "__main__":
    apple = Apple('red')
    apple.grow()
    banana = Banana('yellow')
    banana.grow()
    







        
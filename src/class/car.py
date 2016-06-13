#coding:utf-8
'''
Created on 2016��6��12��
第一种方法：直接使用外部类调用内部类，生成内部类的实例再调用内部类的方法
object_name = outclass_name.inclass_name()
object_name.method()
第二种方法:先对外部类进行实例，然后在实例化内部类，最后调用内部类的方法

out_name = outclass_name()
in_name = out_name.inclass_name()
in_name.method()

@author: Administrator
'''

class Car(object):
    '''
    内部类的调用
    '''
    class Door:
        def open(self):
            print('open door')
            
    class Wheel:
        def run(self):
            print('car run')


    def __init__(self):
        self.door = Car.Door()
        self.wheel = Car.Wheel()
        
        

if __name__ == '__main__':
    car = Car()
    car.door.open()
    car.wheel.run()
#     print(car.__doc__)
    
    door = Car.Door()
    door.open()
        
        
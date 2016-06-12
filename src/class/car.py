#coding:utf-8
'''
Created on 2016��6��12��

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
    print(car.__doc__)
        
        
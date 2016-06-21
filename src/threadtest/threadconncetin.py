#coding:utf-8
'''
Created on 2016年6月21日
@author: Administrator
重写run方法
'''

from threading import Thread,Condition,currentThread
import time


class Goods:
    def __init__(self):   #初始化函数
        self.count = 0
    def produce(self,num = 1): #产品增长
        self.count+=num
    def consume(self):  #产品减少
        self.count -= 1
    def isEmpty(self):
        return not self.count
    
    
#生产者    
class Producer(Thread):
    def __init__(self,condition,goods,sleeptime = 1):
        Thread.__init__(self)
        self.cond = condition
        self.goods = goods
        self.sleeptime = sleeptime
     
    def run(self):
        cond = self.cond
        goods = self.goods
        while 1:
            cond.acquire()
            goods.produce()
            print('Goods Count:',goods.count,'Producer thread prodeced')
            cond.notifyAll()  #通知其他线程
            cond.release()
            time.sleep(self.sleeptime)    
        
        
        
        
class Consumer(Thread):
    def __init__(self,index,condition,goods,sleeptime=1):
        Thread.__init__(self,name = str(index))
        self.cond = condition
        self.goods = goods;
        self.sleeptime = sleeptime
     
    def run(self):
        cond = self.cond
        goods = self.goods
        while 1:
            time.sleep(self.sleeptime)
            cond.acquire()
            while goods.isEmpty():
                cond.wait()
            goods.consume()
            print('Goods count:',goods.count,'Consumer Thread',currentThread().getName())
            cond.release()
            
                            
        
if __name__ == '__main__':
    goods = Goods()
    cond = Condition()
    
    producer = Producer(cond,goods)
    producer.start()
#     producer.join()      不能阻塞主线程，不然无法执行消费程序
    
    for i in range(5):
        consumer = Consumer(i,cond,goods)
        consumer.start()
#         consumer.join()    不能阻塞主线程 不然无法找到 生产者
         
 
         
         
         
                
        
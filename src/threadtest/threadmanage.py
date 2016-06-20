#coding:utf-8
'''
Created on 2016年6月20日
@author: Administrator
'''
'''
1、主线程对子线程的控制
2、线程中的局部变量
'''
import threading,time,random

class ThreadLocal(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.local = threading.local()  #生成local数据对象
    def run(self):
        time.sleep(random.random())  #随机数  线程休眠一段时间
        self.local.number = []
        for _ in range(10):
            self.local.number.append(random.choice(range(10)))
        print(threading.currentThread(),self.local.number)
            

class ThreadSkeleton(threading.Thread):
    def __init__(self,index,creat_time):
        threading.Thread.__init__(self)
        self.index = index
        self.create_time = creat_time
    def run(self):
        print(time.time() - self.create_time,'---->',self.index)
    

if __name__ == '__main__':
    
#     threadLocal = ThreadLocal()
    threads = []
    for i in range(5):
        t = ThreadLocal()
        t.start()
        threads.append(t)
    for i in range(5):
        threads[i].join()
    
    
    
    '''
    threads = []
    for index in range(5):
        thread = ThreadSkeleton(index,time.time())
        thread.start()
        threads.append(thread)
       
    for th in threads:
        th.join()     #等待子线程都执行结束之后，在执行主线程
    print('Mian thread exit...') 
    '''
       
        
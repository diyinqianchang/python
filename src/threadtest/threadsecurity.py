#coding:utf-8
'''
Created on 2016年6月20日
@author: Administrator
'''
'''
线程安全   线程之间的同步
'''
import threading,time


class Counter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()
    def increment(self):
        self.lock.acquire()
        self.value = self.value + 1
        value = self.value
        self.lock.release()
        return value

counter = Counter() 

class ThreadLockDemo(threading.Thread):
    def __init__(self,index,creat_time):
        threading.Thread.__init__(self)
        self.index = index
        self.create_time = creat_time
    def run(self):
        flag = counter.increment()
        time.sleep(1)
        print('  %d----->%d  '%(self.index,flag))
        
        
    
if __name__ == '__main__':
    for index in range(100):
        thread = ThreadLockDemo(index,time.time())
        thread.start()

    
    
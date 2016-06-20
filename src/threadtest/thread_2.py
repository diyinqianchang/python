#coding:utf-8
'''
Created on 2016年6月17日

start  开始运行生成的线程实例
run    重载此方法，作为线程的运行部分
join 等待线程的结束
getName  返回线程的名字
setName  设置线程的名字
isAlive  查看线程是否还是活动
isDaemon
setDaemon  设置线程的后台运行标志

@author: Administrator
'''
import threading,time

class ThreadDemo(threading.Thread):
    def __init__(self,index,create_time):
        threading.Thread.__init__(self)
        print(index)
        self.index = index
        self.create_time = create_time
        
    def run(self):
        time.sleep(1)    #休眠1s钟
        print(time.time()-self.create_time,'--->',self.index)
        print('Thread %d exit...'%(self.index))
        
if __name__ == '__main__':
    for index in range(5):
        thread = ThreadDemo(index,time.time())
        thread.start()
    print('Main Thread exit......')      
        


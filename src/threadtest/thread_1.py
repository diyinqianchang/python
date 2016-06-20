#coding:utf-8
'''
Created on 2016��6��17��

@author: Administrator
'''
import thread,time

def worker(index,create_time):
    time.sleep(1)
    print(time.time() - create_time ,"     ",index)
    print('Thread %d exit...' %index)
    
    
if __name__ == '__main__':    
    for ind in [0,1,2,3,4]:
        try:
            thread.start_new_thread(worker, (ind,time.time()))
        except Exception:
            print('error')
     

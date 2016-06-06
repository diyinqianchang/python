#coding=UTF8


'''
Created on 2016年6月5日
@author: Administrator
'''

# #标准输入流
# import sys
# sys.stdin = open('hello.txt','r')
# for line in sys.stdin.readlines():
#     print(line)
#     
#     
#     
# #标准输出流
# sys.stdout = open('hello.txt','a')
# print(" goodbye")
# sys.stdout.close()


import sys,time
sys.stderr = open('record.txt','a')
f = open('hello.txt','r')
t = time.strftime('%Y - %m - %d %X',time.localtime())
# pt = time.strptime(string, format)
print(t)
context = f.read()
if context:
    sys.stderr.write(t+" "+context)
else:
    raise Exception, t+ " 异常信息"

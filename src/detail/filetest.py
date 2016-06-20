#coding=UTF8
'''
Created on 2016��6��2��

@author: Administrator
'''
#文件的写入
# context = 'hello world hello China hello Keke'
# f = open('hello.txt','a')   #以写入的方式打开文件。先删除文件原有的内容
# #再重新写入新的内容。如果文件不存在，则创建1个新的文件
# f.write(context)
# f.close()
#文件的读取

# f = file("hello.txt",'r')
# while True:
#     line = f.readline()
#     if line:
#         print(line)
#     else:
#         break
# print(f.next())
# f.seek(0,0)
# print(f.readlines())
# print(f.tell())
# f.close()
# print(f.closed)
# print(f.mode)
# print(f.encoding)
#     
# f = file('hello.txt','r')
# lines = f.readlines(1)  #一次可读取文件中多行数据
# for line in lines:
#     print(line)
# f.close() 
# 
# f = open('hello.txt')
# content = f.read()  #一次读完全部内容
# print(content)
# f.close()

import os
# 
# file("hello.txt",'w')
path = 'hello.txt'
if os.path.exists('hello.txt'):
    print('存在')
#     os.startfile('hello.txt','notepad')

absp=os.path.abspath(path)
print(absp.find('.'))
print(absp)
print(os.path.split(path))
print(os.path.splitext(path))
print(os.path.isfile('hello.txt'))
print(os.path.isdir(path))
# os.F_OK 
# 作为access()的mode参数，测试path是否存在. 
# os.R_OK 
# 包含在access()的mode参数中 ， 测试path是否可读. 
# os.W_OK 
# 包含在access()的mode参数中 ，测试path是否可写. 
# os.X_OK 
# 包含在access()的mode参数中 ，测试path是否可执行.. 
fl = os.access('hello.txt',os.F_OK)
print(fl)


# 
# print(os.listdir('.'))   #返回目录下的所有文件
# print(os.path.abspath('hello.txt'))   #返回文件的绝对路径
    
#文件的复制   也可以 read和write做
# import shutil
# shutil.copyfile('hello.txt', 'hello1.txt')

#文件重命名  先找出当前目录的文件列表
# import os
# li = os.listdir('.')
# if 'hello1.txt' in li:
#     os.rename('hello1.txt','hi.txt')
# elif 'hi.txt' in li:
#     os.rename('hi.txt', 'hello3.txt')

#修改文件后缀名
# files = os.listdir('.')
# for filename in files:
#     li = os.path.splitext(filename)
#     print(li) 
#     if li[1] == '.html':
#         newname = li[0]+'.txt'
#         os.rename(filename, newname)

 
#用于路径的匹配
import glob
li = glob.glob('*.txt')
print(li)

#文件查找
# import re
# f1 = open('hello.txt','a+')    #打开文件
# count = 0
# for s in f1.readlines():      #按行读取文件内容
#     li = re.findall('hello', s, re.IGNORECASE)   #匹配文件
#     print(li)
#     if len(li)>0:
#         count = count + li.count('hello')
#     f1.write(s.replace('hello','hi')+'\n')  #替换内容
# print('查找到'+str(count)+'个hello')
# f1.close()

#文件的比较
# import difflib
# f1 = file('hello.txt','r')
# f2 = file('hello3.txt','r')
# src = f1.read()
# dst = f2.read()
# print(src)
# print(dst)
# 
# s = difflib.SequenceMatcher(lambda x:x=='',src,dst)
# for tag,i1,i2,j1,j2 in s.get_opcodes():
#     print('%s src(%d:%d)=%s dst[%d:%d]=%s'%(tag,i1,i2,src[i1:i2],j1,j2,dst[j1:j2])

# 配置文件  没有细看
# import ConfigParser
# config = ConfigParser.ConfigParser()
# config.read('ODBC.ini')
# sections = config.sections()
# print(sections)
# o = config.options('ODBC 32 bit Data Sources')
# print("配置项:",o)


# import os
# os.mkdir('hello')
# os.rmdir('hello')

# 文件遍历

# def VisitDir(path):
#     li = os.listdir(path)
#     for p in li:
#         pathname = os.path.join(path,p)
#         if not os.path.isfile(pathname):
#             VisitDir(pathname)
#         else:
#             print(pathname)
#             
# 
# 
# 
# def VisitDir1(path):
#     for root,dirs,files in os.walk(path):
#         print('************')
#         print(dirs)#目录列表
#         print('************')
#         print(root) #路径名
#         print('************')
#         for filepath in files:  #files 文件列表
#             print os.path.join(root,filepath)
#     
#     
# path = r'C:\Users\Administrator\Desktop\Java\PythonDetail'
# VisitDir1(path)





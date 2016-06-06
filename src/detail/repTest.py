#coding:UTF8
'''
Created on 2016��6��1��
@author: Administrator
'''
import re
 
x = 'HELLO WORLD'
print(re.findall("hello", x,re.IGNORECASE))
print(re.findall("WORLD$", x, re.IGNORECASE))
#有转义字符
print(re.findall(r"\b\w+\b", x))
#sub先创建原变量的拷贝，然后在拷贝中替换字符串，并不会改变变量s的内容
print(re.sub("HELLO", "hi", x, 0, re.IGNORECASE))

s = '你好 WORLD2'
print('匹配字母数字'+re.sub(r"\w", "hi", s))
print("替换次数"+str(re.subn(r"\w", "hi", s)))
print("匹配非字母数字"+re.sub(r"\W", "hi", s))
print("匹配非字母数字"+re.sub(r"\s", "*", s))

s1 = '1abc23def45'
p = re.compile(r'\d+')
print(p.findall(s1))
print(p.pattern)
print(re.findall(r"\d+", s1))

pre = re.compile(r"(abc)\1")
m = pre.match("abcabc")
print(m.group(0))  #返回整个表达式
print(m.group(1))

#没有见过这种匹配  (?P<one>abc)给分组命名 one (?P=one)调用分组
pre2  = re.compile(r"(?P<one>abc)(?P=one)")
ma = pre2.search("abcabc")
print(ma.group("one"))

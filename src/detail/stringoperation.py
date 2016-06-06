#coding:UTF8

#字符串的格式化
import operator
str1 = 'version'
num = 1.0
myformat = "%s" %str1
print(myformat.center(20,"*"))
print(myformat.ljust(10,"*"))

print("浮点数:%.2f"%1.254)

#字符串的转义字符

path = "\thello world\n"
print(path)
print(len(path))
print ("输出:"+path.strip())
print("输出:"+path.lstrip())

#字符串的合并

strs = ['hello ','world ','hello ','China ']
result = " ".join(strs)
print(result)

print(result[12::])

op = reduce(operator.add, strs,"  ")
print("====>>", op)




#字符串的比较

word = 'hello world'
print('hello' == word[0:5])
print(word>'tyt')
print(word.startswith('hello'))
print(word.endswith('ld',6))


#字符串反转
wordlist = ['hello','world']
wordlist.reverse()  #reverse() 没有返回值， 原有的list改变了
print(" ".join(wordlist))

#字符串的查找
sentence ="This is a apple"
print(sentence.find("a"))
sentence ="This is a apple"
print(sentence.rfind('a'))


#字符串的替换 replace()先创建变量的拷贝，然后在拷贝中替换字符串
#不会改变变量的值
centence = "hello world, hello China"
print(centence.replace("hello", "hi"))
print(centence.replace("hello", "hi",1))
print(centence)


#字符串和日期的转换
import time
#时间到字符串
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))







#coding:utf-8
'''
Created on 2016年6月5日
@author: Administrator
'''

# 
# #元祖
# tuple_name = ('apple','banana','grape')
# 
# #元组的遍历
# for t in map(lambda x:x+' 1', tuple_name):
#     print(t)
# 
# 
# for a in range(len(tuple_name)):
#     print(tuple_name[a])
# 
# print(tuple_name[0])
# print(tuple_name[0:2])
# #元组解包
# a,b,c = tuple_name
# print(a,b,c)
# tu = ((1,2),(3,4))
# print(tu)

#List

list1 = ['apple','banana','orange','grape']
print(list1)
list1.append('watermelon')
list1.insert(0, 'pare')
print(list1)

print(list1.pop())
print(list1)

print(list1[::-1])
for i in xrange(len(list1)-1,-1,-1):
    print(list1[i])
list1.sort(reverse=True)
print(list1)
print("apple" in list1)



list2 = ['cat','dog','pig']

list1.extend(list2)
print(list1+list2)














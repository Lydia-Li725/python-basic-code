str1 = 'aabbccdd'
str2 = 'bb'

list1 = [1,2]
list11 = ['a','b','c','d','e']
list2 = [10,20]

t1 = (1,2)
t2 = (10,20)

d1 = {'name': "python"}
d2 = {'age':30}

# 加号运算符：合并 字典不支持合并
print(str1+str2)
print(list1+list2)
print(t1+t2)

# 乘号：复制 字典不支持
print(str1*5)
print('-'*10)
print(list1*5)
print(t1*5)

#in  not in是否存在
print('a' in str1)
print(2 in list1)
print(3 in t1)
print('name' in d1)
print('name' in d1.keys())
print('name' in d1.values())

#len
print(len(list1))
print(len(str1))
print(len(t1))
print(len(d1))

#del
#del str1
#print(str1)
del list1[0]
print(list1)

del d1['name']
print(d1)

#max
print(max(str1))
print(min(str1))
print(min(list1))
print(max(list1))

#range
for i in range(1,10,1):
    print(i)

#enumerate#返回元组，第一个数据为下标，第二个为原迭代对象的数据
for i in enumerate(list11):
    print(i)

for i in enumerate(list11, start=1):
    print(i)


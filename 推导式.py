#只有列表字典集合：化简代码
##列表推导式
list1 = []
#利用while循环创建0-10的列表
i = 0
while i <10:
    list1.append(i)
    i += 1
print(list1)
#for循环
list2 = []
for i in range(10):
    list2.append(i)
    i += 1
print(list2)

#列表推导式
list3 = [i for i in range(10)]
print(list3)

#带if的列表推导式
l1 = [i for i in range(10) if i%2 ==0]
print(l1)

#多个for循环
#for循环嵌套
l4 = []
i = range(1,3)
j = range(3)
for i in range(1,3):
    for j in range(3):
        l4.append((i,j))
print(l4)
# 多for推导式等同于for嵌套
l2 = [(i,j) for i in range(1,3) for j in range(3)]
print(l2)

#字典推导式
#创建一个字典，key1-5,value为前面平方
dict1= {i: i**2 for i in range(1,5)}
print(dict1)

#两个列表合并为字典
list11 = ['name','age','gender']
list12 = ["TOM",20,"male"]
dict2 = {list11[i]: list12[i] for i in range(len(list12))}
print(dict2)

# 如果两个列表数据个数相同，len统计任何一个列表个数都可以
#如果不相同，len统计多的会报错，len统计少的不会报错

#提去字典中的目标数据
counts = {'mbp': 268,'HP':125,'DELL':201,'lenove':199}
count1 = {key: value for key,value in counts.items() if value >= 200}
print(count1)

#集合推导式
listi = [1,1,2]
set1 = {i**2 for i in listi}
print(set1)
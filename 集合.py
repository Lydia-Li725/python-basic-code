# 有数据的集合
s1 = {10,20,30}
print(s1)#没有顺序

s2 = set('abcdefg')
print(s2)
#空集合
s4 = set()
print(type(s4))

#增加
#add追加单一数据
s1.add(100)
print(s1)#集合可变类型
#update追加数据序列
s1.update([10,20,30,40,50])
print(s1)
#remove
s1.remove(10)
print(s1)

#s1.remove(10000)#报错
print(s1)

s1.discard(20)
print(s1)

s1.discard(20)
print(s1)

delnum = s1.pop()
print(delnum)
print(s1)

print(10 in s1)
print(10 not in s1)
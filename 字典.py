d1 = {'name': 'Tom', 'age': 20, 'gender': 'male'}
print(d1)
print(type(d1))

d2 ={}
d3 = dict()
print(type(d2))
print(type(d3))

#新增
d1['id'] = 110
print(d1)
d1['name'] = 'rose'
print(d1)
# 删除
#del d1['name']
print(d1)

#d1.clear()
print(d1)

#查找
print(d1['name'])
#get
print(d1.get('name'))
print(d1.get('iid',190))
print(d1.get('iid'))
#keys查找字典中所有key，返回可迭代对象
print(d1.keys())#可调用
# values 查找所有值，返回可迭代对象
print(d1.values())

#items 查找所有的键值对，返回可迭代对象，里面为元组，1为key，2为值
print(d1.items())


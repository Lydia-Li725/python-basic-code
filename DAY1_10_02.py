"""
1.按经验将不同的变量存储不同类型的数据

2.验证这些数据是什么类型--检测数据类型-type(数据)
"""
# int--整型
num1 = 1

# float 浮点型
num2 = 1.1
print(type(num1))
print(type(num2))

# str--字符串
a = 'hello world'
print(type(a))

# bool--布尔型
b = True
print(type(b))

# list--列表,方括号
c = [10,20,30]
print(type(c))

# tuple--元组，小括号
d = (1,2,3)
print(type(d))

# set--集合，大括号
d = {1,2,3}
print(type(d))

# dict--字典--键值对
f = {'name':'Tom','AGE':18}
print(type(f))

'''
格式化输出
1.准备数据
2.格式化输出数据
'''
age = 18
name = "TOM"
weight = 75.5
stu_id = 1
stu_id2 = 1000
print('今年我的年龄是%d岁' % age)
print('我的名字是%s' % name)
print('我的体重是%.2f公斤' % weight)
print('我的体重是%f公斤' % weight)
print('我的学号是%d' % stu_id)
print('我的学号是%03d' % stu_id)
print('我的学号是%03d' % stu_id2)

print('我的名字是%s.我的年龄是%d岁' % (name,age))
print('我的名字是%s.我的年龄是%d岁' % (name,age + 1))
print('我的名字是%s.我的年龄是%s岁.我的体重是%s' % (name,age ,weight))
# %s可以输出各种类型

#f格式化字符串
print(f'我的名字是{name},今年{age}岁了')
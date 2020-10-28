a = 'l'
b = "l1"
c = '''l
l'''
print(type(a))
print(type(b))
print(type(c))
print(c)

d = 'I\'m Tom'
print(d)

# 字符串格式化输出
name = 'Rose'
print('My name is %s' % name)
print(f'my name is {name}')

# 字符串输入
name = input("您的名字是：")
print(f'您输入了{name}')
print(type(name))
'''
1.input
2.检测input数据类型
3.int() 转换数据类型
4.检测是否转换成功
'''

num = input('输入数字：')
print(num)

print(type(num))

print(type(int(num)))

num1 = 1
str1 = 10

print(type(float(num1))) #float
print(float(str1)) #10.0

print(type(str(num1)))

list1 = [10,20,30]
print(type(tuple(list1)))

t1 = (100,200,400)
print(type(list(t1)))

#eval() 计算在字符串中的有效python表达式，并返回一个对象

str2 = '1'
str3 = '1.1'
str4 = '(10,20,30)'
str5 = '[33,45,60]'
print(type(eval(str2)))
print(type(eval(str3)))
print(type(eval(str4)))
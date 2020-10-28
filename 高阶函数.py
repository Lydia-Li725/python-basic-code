#绝对值
print(abs(-100))

#四舍五入
print(round(1.4))

#将函数作为参数放入其他函数
def ab_num(a,b,f):
    return f(a)+f(b)

a_n = ab_num(1,-9,abs)
print(a_n)

#map
#map(func,lst) 将函数func作用于lst列表返回迭代器结果
list1 = [1,4,7,9]

def fun(x):
    return x**2
result = map(fun,list1)
print(result)
print(list(result))

#reduce
#reduce(func,lst)其中函数必须有两个参数，每次func计算结果继续与下一个元素累积计算
#导入模块
import functools

def func(a,b):
    return a+b

result = functools.reduce(func,list1)
print(result)

#filter （func，lst）过滤不符合条件的元素，返回一个filter对象。如要转换为列表，使用list转换

def f_filter(x):
    return x%2 ==0

re2 = filter(f_filter,list1)
print(re2)
print(list(re2))
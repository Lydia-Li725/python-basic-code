#简化代码：如果一个函数有一个返回值，并且只有一句代码，可以利用lambda简化
#def
def fn1():
    return 100

#lambda 匿名函数
fn2 = lambda: 100
print(fn2)

print(fn2())

#列表数据按字典key的值排序
students = [{'name':'tom','age':20},
            {'name':'amy','age':21},
            {'name':'rose','age':22}
 ]

#按name值升序排列

students.sort(key=lambda x:x['name'])

print(students)
#按name降序
students.sort(key=lambda x:x['name'],reverse=True)
print(students)

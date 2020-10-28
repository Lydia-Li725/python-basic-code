age = 20
if age >= 18:
    print("已经成年")

print("系统关闭")# 与条件语句无关

'''
1.用户输入
2.保存输入的年龄
3.if
有一个点需要注意:input接受的数据是str类型不能与18做判断，需要将它转化为int类型
'''
age = int(input("请输入您的年龄："))

if age >= 18:
    print(f'您输的年龄是{age},成年')

if age >= 18:
    print(f'您输的年龄是{age},成年')
else:
    print(f'你只有{age}岁，不能去')


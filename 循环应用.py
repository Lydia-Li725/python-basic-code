'''
1.打印一个星星
2.循环五个在一行显示
3.循环五行
'''
j = 0
while j < 5:
    #一行星星
    i = 0
    while i < 5:
        print("*",end='')#一个星星后面不换行，print 默认会换行
        i += 1
        #一行星星结束，下一行开始
    print()#一行结束换行，利用print换行
    j += 1

#打印三角形星号
'''
每行星星个数i和行号j一样
'''
j = 0
while j < 5:
    #一行星星
    i = 0
    while i <= j:
        print("*",end='')#一个星星后面不换行，print 默认会换行
        i += 1
        #一行星星结束，下一行开始
    print()#一行结束换行，利用print换行
    j += 1

# 九九乘法表
'''
多行多个乘法表达式
1.打印一个表达式
2.一行多个表达式 个数和行号相等 循环一个表达式
3.打印多行表达式 循环一行表达式
4.每行之间换行'''
j = 1
while j <= 9:
    #一行的表达式
    i = 1
    while i <= j: # 联动关系
        print(f'{i} * {j} = {i*j} ',end = "\t" ) # \t可以对齐
        i += 1
        #一行结束
    print()#换行
    j += 1
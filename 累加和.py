'''
需求：1-100数字累加和 1+2+..+100=结果 打印结果

1.准备加法的数据1-100增量为1
2.准备变量保存结果
3.循环加法
4.打印结果
5.验证结果
'''

# 准备数据
i = 1
# 准备变量存结果
s = 0
# 循环
while i <= 100:
    s += i
    i += 1

print(s)

# 偶数累加和
'''
1.准备累加的数字 1-100，增量是1
2.准备结果变量
3.循环加法运算，偶数才运算，和2取余数为0
4.输出结果
5.验证结果
'''
i = 1
r = 0
while i <=100:
    if i%2 == 0:
        r += i
    i += 1

print(r)

# 计数器
i = 0
s = 0
while i <= 100:
    s += i
    i += 2

print(s)
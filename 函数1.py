# 1.搭建框架 由于先定义再调用，所以23在1上面
# 2.确实选择功能界面
# 3，封装函数
# 4.在需要的位置调用函数
def sel_func():
    print('显示余额')
    print('存')
    print('取')

print('登陆成功')
sel_func()
#显示功能
print('密码是：11111111')
sel_func()
#显示功能
print('取了100')
sel_func()
#显示功能

#定义函数
def info_p():
    print("hello world")
#调用函数
info_p()
'''
1.先定义后调用
先调用会报错
2.没有调用函数，函数的代码不会执行
3.函数执行流程：调用函数时会回到定义函数执行代码，之后回到调用函数执行，定义函数时，函数体内部缩进不执行
'''


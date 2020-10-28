'''
1.打开open
2.读写
3.关闭文件（不关闭一直在内存中）

open函数:open(name,mode)
name为打开的目标文件名的字符串
mode设置打开文件的模式：只读、写入、追加等
'''
#1.打开open
f = open("text,txt",'w')

#2.读写
f.write('aaa')

#3.关闭文件（不关闭一直在内存中）
f.close()

"""
测试目标
1.访问模式对文件的影响
"""
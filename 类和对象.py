'''
先有类再有对象
#类名要满足标识符命名规则同时遵循大驼峰命名习惯
用类去创建对象

class 类名（）：
    代码
'''

#创建类
class washer():
    def wash(self):
        print('能洗衣服')

#创建对象
haier = washer()

#验证成果
#打印
print(haier)
#使用功能--实例方法（对象方法：对象名.wash()
haier.wash()

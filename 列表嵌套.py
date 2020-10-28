# 十个班，每个班的名字存在一个子列表中，将十个班放在一个大列表

name_list = [['a','b','c'],['tom','amy','lily'],['小红','小黄','小李']]
print(name_list)

#数据查询
print(name_list[0][0])

# 8个老师，分配三个办公室
'''
步骤：
1.准备数据
    1.8个老师名字-列表
    2.三个办公室-列表嵌套
2.分配老师到办公室-随机-办公室列表追加老师名字
3.是否分配成功
'''
import random
#准备数据
teachers = ['a','b','c','d','e','f','g','h']
offices = [[],[],[]]
#分配办公室
for name in teachers:
    num = random.randint(0,2)
    offices[num].append(name)
print(offices)
i = 1
for office in offices:
    print(f'办公室{i}的人数是{len(office)},老师分别为：')
    for name in office:
        print(name)
    i += 1
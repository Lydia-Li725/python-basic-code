
def info_p():
    print('-'*20)
    print('1、添加')
    print('2、删除')
    print('3、修改')
    print('4、查询')
    print('5、显示所有')
    print('6、退出')
    print('-'*20)

#等待存储所有学员的信息
info = []

#添加学员信息的函数：
def add_info():
    '''添加学员函数 '''

    #1.用户输入学号姓名手机号

    #2.判断是否添加这个学员：如果姓名存在报错，不存在添加数据


    new_id = input("输入学号")
    new_name = input("输入姓名")
    new_tel = input("输入电话")

    global info
    #检测用户输入的姓名存在，则报错
    for i in info:
        if new_name == i['name']:
            print("用户存在")
            return#代码不执行
    # 如果用户不存在，添加学员信息
    info_dict = {}
    # 将用户输入的数据追加到字典
    info_dict['id'] = new_id
    info_dict['name'] = new_name
    info_dict['tel'] = new_tel

    # 将这个学员的字典数据追加到列表
    info.append(info_dict)
    print(info)

# 删除学员
def del_info():
    '''删除学员'''
    #1.输入要删除的学员姓名
    del_name = input("请输入姓名：")

    # 2.检查需要删除的学员是否存在：存在删除，不存在提示
    # 2.1 声明info全局变量
    global info
    # 2.2遍历列表
    for i in info:
    #2.3 判断是否存在：存在删除，break 不允许重名，删除一个不需要再遍历其他的
        if del_name == i['name']:
            info.remove(i)
            break
    else:
        print('学员不存在')

    print(info)

#修改学员信息
def modify_info():
    '''修改学员信息'''
    #1.输入想要修改的姓名
    modi_name = input("请输入需要修改的姓名：")
    #2.判断是否存在，遍历，如果存在就改不存在就报错
    global info
    for i in info:
        if modi_name == i['name']:
            i['tel'] = input("输入新的手机号：")
            break
        else:
            print("用户不存在")

    print(info)

#查询
def search_info():
    '''查询学员信息'''
    #1.输入需要查询的学员姓名
    s_name = input("请输入需要查询的名字：")
    #2.遍历看是否存在，存在显式信息，不存在报错
    global info
    for i in info:
        if s_name == i['name']:
            print(f"用户习惯名为{i['name']},id为{i['id']},手机号为{i['tel']}")
            break
    else:
        print("用户不存在")

#显示所有学员信息
def p_all():
    print('学号\t姓名\t电话')
    for i in info:
        print(f"用户名为{i['name']}\tid为{i['id']}\t手机号为{i['tel']}")
# 循环使得到输入6才退出
while True:
    info_p()

    user_name = int(input('请输入序号：'))

    if user_name == 1:
        add_info()
    elif user_name == 2:
        del_info()
    elif user_name == 3:
        modify_info()
    elif user_name == 4:
        search_info()
    elif user_name == 5:
        p_all()
    elif user_name == 6:
         #现有想结束
         exit_flag = input("确定退出？yes no")
         if exit_flag == "yes":
             break
    else:
        print("输入有误")

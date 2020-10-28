# 函数返回值 返回位置：函数调用的位置
def return_num():
    return 100

result = return_num()
print(result)

#递归特点：函数内部 自己调用自己；必须有出口

def sum_numbers(num):
   #出口
    if num == 1:
        return 1
    #当前数字+当前数字减一累加
    return num + sum_numbers(num-1)

re = sum_numbers(6)
print(re)
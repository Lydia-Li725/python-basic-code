# 坐公交车，有钱上车，否则不上，如果上车有空座坐下
'''
1.做准备：钱和空座位
2.判断有钱：有 上车
2.有座位
'''

money = 1
seat = 0
if money == 1:
    print("上车")
    if seat == 1:
        print("可以坐")
    else:
        print("站着")
else:
    print("不能上车")
# break:当某些条件成立退出整个循环
#吃到第三个就饱了，4和5就不吃了

i = 1
while i <= 5:
    #如果大于3就不吃了
    if i > 3:
        break
    print(f'吃了{i}个苹果')
    i += 1
print("不吃了")
# continue 条件成立退出当前循环执行下一次循环
i = 1
while i <=5:
    if i ==3:
        print("吃出虫子，不吃了")
        # 使用continue，在continue之前修改计数器
        i += 1
        continue

    print(f'吃了第{i}个苹果')
    i += 1

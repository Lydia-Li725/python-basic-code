str1 = 'ilxy'
for i in str1:
    print(i)

str1 = 'ilxy'
for i in str1:
    if i == 'l':
        print("dead")
        break
    print(i)

str1 = 'ilxy'
for i in str1:
    if i == 'l':
        print("die again")
        continue
    print(i)
#正常执行 while+else
i = 1
while i <= 5:
    print("我错了")
    i += 1
else:
    print("good")
#else正常结束循环才能执行，一次不对直接结束 while+else+break
i = 1
while i <= 5:
    print("我错了")
    if i ==3:
        print("die")
        break
    i += 1
else:
    print("good")
#一次不对下次继续 while+else+continue
i = 1
while i <= 5:
    print("我错了")
    if i == 3:
        print("bad")
        i += 1
        continue
    i += 1
else:
    print("good")
#for+else
for i in str1:
    print(i)
else:
    print("hhh")
# for+break+else
for i in str1:
    if i =='l':
        print("no")
        break
    print(i)
else:
    print("hhh")
#for + continue +else
for i in str1:
    if i =='l':
        print("no")
        continue
    print(i)
else:
    print("hhh")
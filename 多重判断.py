age = int(input("输入您的年龄:"))
# 童工
if age < 18:
    print(f'您的年龄是{age},童工')
# 合法 可以简化为 18 <= age <= 60
elif 18 <= age <= 60:
    print(f'您的年龄是{age},合法')
# 退休
else:
    print(f'您的年龄是{age},老年人')

d1 = {'name': 'Tom', 'age': 20, 'gender': 'male'}
# 遍历keys
for key in d1.keys():
    print(key)

#遍历values
for value in d1.values():
    print(value)

#遍历元素
for item in d1.items():
    print(item)

# 遍历键值对，拆包
for key,value in d1.items():
    print(f'{key} = {value}')
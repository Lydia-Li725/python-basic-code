n_l =['TOM','LILIY','LINDA']
'''print(n_l)
print(n_l[0])
print(n_l[2])

print(n_l.index('LILIY'))
#print(n_l.index('Tom'))
print(n_l.count('TOM'))
print(len(n_l))
print('TOM' in n_l)
print('l'not in n_l)
#注册邮箱，判断是否存在账户名
#name = input("请输入名字：")'''
'''
if name in n_l:
    print(f'您的名字是{name},从新输入')
else:
    print('ok')'''
#append extend
'''n_l.append('amy')
print(n_l)
n_l.append([11,22])
print(n_l)
n_l.extend("xiaoming")
print(n_l)
n_l.extend([11,222])
print(n_l)
n_l.insert(1,"aaa")
print(n_l)'''
#del
'''del n_l
print(n_l)'''
#pop
'''d_n = n_l.pop()
print(d_n)
print(n_l)'''

'''n_l.remove('TOM')
print(n_l)'''

'''n_l.clear()
print(n_l)'''

n_l[0] = "aa"
print(n_l)

list1 = [1,23,5,6,7]
list1.reverse()
print(list1)

list1.sort()
print(list1)

list1.sort(reverse=True)
print(list1)

n_l3 = n_l.copy()
print(n_l3)
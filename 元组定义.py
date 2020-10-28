t1 = (10,20,30)
print(type(t1))

t2 = (10,)
print(type(t2))

t3 = (10)
print(type(t3))

t4 = ('aa','bb','cc','dd')
#下标
print(t4[0])
#index
print(t4.index("bb"))
#count
print(t4.count("aa"))
#len
print(len(t4))

t11 = ('a',['ab','ac'],'d')
t11[1][0] = 'tom'
print(t11)
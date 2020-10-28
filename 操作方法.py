mystr = "hello world and my life sucks and python is so hard"

#1.find
print(mystr.find("and",20,40))
print(mystr.find("ands",20,40))#不存在-1
#index
print(mystr.find("and",20,40))
#print(mystr.find("ands",20,40))# 报错

#count
print(mystr.count("and",15,30))
print(mystr.count("ands",15,30))#返回0
#rfind
print(mystr.rfind("and"))

#rindex
print(mystr.rindex("and"))


##修改
#replace 替换
print(mystr.replace("and","he"))
#调用replace之后原有字符串的数据并没有做到修改，修改后的数据是replace函数的返回值
# 字符串是不可修改数据
# 数据根据是否可以改变分为可变类型和不可变类型
print(mystr.replace("and","he",1))
print(mystr.replace("and","he",10))

#split()分割返回一个列表
list1 = mystr.split("and")
list2 = mystr.split("and",1)
print(list1)
print(list2)

#join
mylist = ['aa','bb','cc']
abc = '...'.join(mylist)
print(abc)

print(mystr.capitalize())
print(mystr.title())
print(mystr.upper())
print(mystr.lower())

mystr1 = "  kkkkkkkllllll    "
print(mystr1.lstrip())
print(mystr1.rstrip())
print(mystr1.strip())

print(mystr.startswith("and",20,50))
print(mystr.endswith("world"))
print(mystr.endswith("hard"))

mystr3 = "hello12344"
print(mystr3.isalpha())
print(mystr.isalpha())
print(mystr3.isdigit())
print(mystr.isalpha())
print(mystr3.isalnum())

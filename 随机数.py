import random


player = int(input("出拳:，0--石头，1--剪刀，2--布:"))
computer = random.randint(0,2)
#print(computer)
# 2.判断输赢
if ((player == 0) and (computer ==1)) or ((player ==1) and (computer ==2)) or ((player ==2) and (computer ==0)):
    print("win")

elif player == computer:
    print("even")

else:
    print("lose")

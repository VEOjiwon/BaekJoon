
#Binary christmas tree
import random
tree_len = 40
tmp = tree_len-1
tmp_1=""
t2=0
for i in range(0,tmp):
    print(" " * tmp, end='', sep="")
    while t2<(i*2 + 1):
        tmp_1=tmp_1+str(random.randrange(0,2))
        t2+=1
    print(tmp_1)
    tmp-=1
for i in range(0,2):
    print(" " * int((tree_len)-2), end='', sep="")
    print("*"*2)
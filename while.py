"""
while문
"""


"""
#A + B - 5
import sys
while True:
    l=list(map(int,sys.stdin.readline().rstrip().split()))
    if l[0] and l[1] !=0 :
        print(l[0]+l[1])
        continue
    else:
        break
###############################################

# A+B - 4
import sys
while True:
    l=list(map(int,sys.stdin.readline().rstrip().split()))
    if not l:
        break
    print(l[0]+l[1])

###############################################
"""

#더하기 싸이클
target = int(input())
temp = target
cnt = 0
while True:
    if int(temp / 10) ==0:
        first_num=temp
        second_num=0
    else :
        first_num = temp %10
        second_num = int(temp /10)
    sumof_fs = first_num + second_num
    #print(first_num,second_num,sumof_fs)
    if sumof_fs>10:
        new_num = int(sumof_fs%10) + first_num*10
    elif sumof_fs == 10:
        new_num = first_num * 10
    else:
        new_num = sumof_fs + first_num * 10
    #print(new_num)
    cnt+=1

    if new_num == target:
        print(cnt)
        break
    else:
        temp = new_num
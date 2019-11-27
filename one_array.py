"""
1 차원 배열
"""
import sys

from pip._vendor.distlib.compat import raw_input

"""
#최대 최소값
import sys
length = int(sys.stdin.readline())
l = list(map(int,sys.stdin.readline().rstrip().split()))
max = -1000000
min = 1000000
for i in l:
    if max<=i:
        max=i
    if min>=i:
        min=i

print(min,max)

###############################################33


#최대값구하는 문제 
l = list()
cnt = 1
max_cnt=0
max=0

#입력부
for i in range(0,9):
    l.append(int(input()))

#최대값 비교부
for i in range(0,9):
    if max < l[i]:
        max_cnt=cnt
        max = l[i]
    cnt+=1
print(max, max_cnt,sep="\n")

###############################################33

#음계
import sys
l = list(map(int,sys.stdin.readline().split()))
asccnt=0
descnt=0

for i in range(0,7):
    if(l[i]<l[i+1]):
        asccnt+=1
    elif(l[i]>l[i+1]):
        descnt+=1

if asccnt==7:
    print("ascending")
elif descnt==7:
    print("descending")
else:
    print("mixed")
    
###############################################33

#숫자의 개수
a = int(input())
b = int(input())
c = int(input())

product = a*b*c
output =[0,0,0,0,0,0,0,0,0,0]
i=10

for i in str(product):
    output[int(i)]+=1

for j in output:
    print(j)

###############################################33

#나머지 (서로다른 값 개수 구하기)
import sys
in_array = []
Remainder = []

fin_cnt=0
for i in range(0,10):
    tmp=0
    tmp = int(input())
    Remainder.append(tmp%42)

t = list(set(Remainder))
print(len(t))

###############################################33


#평균조작하기 

lenof = int(input())
l = list(map(int,sys.stdin.readline().rstrip().split()))
max_num = max(l)
new_l=list()
tmp=0
for i in l:
    new_l.append(i/max_num*100)

for i in new_l:
    tmp+=i
avr = tmp / len(new_l)

print("%0.2f"%(avr))

###############################################33
"""""

#ox퀴즈

test_case = int(input())
a=[]
for i in range(0,test_case):
    a.append(input())
tmpcnt = 0
score=0
for i in a:

    for j in i:
        if j == 'O':
            tmpcnt+=1
            score+=tmpcnt
        else :
            tmpcnt = 0

    print(score)
    score = 0
    tmpcnt=0

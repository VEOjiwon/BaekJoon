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
"""

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
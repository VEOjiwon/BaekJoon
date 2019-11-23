"""
백준 for
"""
"""
#구구단(2739번) 입력받은 수의 구구단 출력하기

num = int(input())
for i in range(1,10):
    print(num,"*",i,"=",num*i)

#########################################################

#2번 a+b-3
num = int(input())
for i in range(0,num):
    a, b = input().split()
    a = int(a)
    b = int(b)
    print(a+b)
    
############################################################


#3번 1부터 n까지 합 구하

x = int(input())
output =0;
for i in range(1,x+1):
    output=output+i
print(output)


############################################################


import sys

num = int(input())
for i in range(0,num):
    L = list(map(int,sys.stdin.readline().rstrip().split()))
    print(L[0]+L[1])

############################################################


#n찍기
x  = int(input())
for i in range(1,x+1):
    print(i)

############################################################

# 기찍 n
x  = int(input())
temp=x
for i in range(1,x+1):
    print(temp)
    temp=temp-1
    
############################################################


#A+B-7
import sys
case = int(input())
for i in range(1,case+1):
    L = list(map(int,sys.stdin.readline().rstrip().split()))
    print("Case #",i,": ",L[0]+L[1],sep="")


###############################################

#A+B-8
import sys
case = int(input())
for i in range(1,case+1):
    L = list(map(int,sys.stdin.readline().rstrip().split()))
    print("Case #",i,": ",L[0]," + ",L[1]," = ",L[0]+L[1],sep="")
    
###############################################

#별찍기 - 1
count = int(input())

for i in range(0,count):
    print("*"*(i+1))

################################################

#별찍기 - 2
count = int(input())
tmp=count-1
for i in range(0,count):
    print(" "*tmp,end='',sep="")
    print("*"*(i+1))
    tmp=tmp-1

###############################################

"""
#x보다 작은 수

n,target= input().split()
n = int(n)
target = int(target)
L = list(map(int, input().split()))
count = 0

for i in range(0,n):
    if(L[i]<target):
        print(L[i],"",end="")
"""
백준 for
"""
""""
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

"""
import sys

num = int(input())
for i in range(0,num):
    L = list(map(int,sys.stdin.readline().rstrip().split()))
    print(L[0]+L[1])
#L = list(map(int, input().split()))
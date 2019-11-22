"""
백준 for
"""
""""
#구구단(2739번) 입력받은 수의 구구단 출력하기

num = int(input())


for i in range(1,10):
    print(num,"*",i,"=",num*i)
"""

#2번 a+b-3

num = int(input())
for i in range(0,num):
    a, b = input().split()
    a = int(a)
    b = int(b)
    print(a+b)
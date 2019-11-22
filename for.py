"""
백준 for
"""

#구구단(2739번) 입력받은 수의 구구단 출력하기

num = int(input())


for i in range(1,10):
    print(num,"*",i,"=",num*i)
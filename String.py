"""
백준 문자열문제 모음
"""

"""
#아스키코드 변환
target = input()
print(ord(target))

################################


#숫자의 합
numbers = int(input())
target = input()
sum=0
for i in target:
    sum+=int(i)

print(sum)

################################


#단어의 합
from string import ascii_lowercase
target = input()
output =[-1 for i in range(26)]
alpha = list(ascii_lowercase)

for idx, val in enumerate(alpha):
    tmp=target.find(val)
    output[idx]=tmp

out = ''
for i in output:
    out+=str(i)+' '
print(out)

################################

#문자열 반복
testcase = int(input())
for i in range(testcase):
    a, b = input().split()
    a = int(a)
    c=''
    for j in b:
        c+=j*a
    print(c)
################################


#단어공부
from string import ascii_uppercase
target = input()
target = target.upper()

alpha = list(ascii_uppercase)
out =''
maxnum = 0
for i in alpha:
    if target.count(i)>maxnum :
        maxnum = target.count(i)
        out = i
    elif maxnum >0 and maxnum == target.count(i):
        out='?'

print(out)

################################
"""

#단어의 개수
target = input()

print(len(list(map(str,target.split()))))

print(len(target.split()))

"""
백준 문자열문제 모음
"""
from typing import List

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

#단어의 개수
target = input()

print(len(list(map(str,target.split()))))

print(len(target.split()))

################################


#상수

a,b = input().split()
a=int(a[::-1])
b=int(b[::-1])

print(max(a,b))

# 한줄짜리 코드... print(max(input()[::-1].split()))

################################

#다이얼
di = {('A','B','C'):3,('D','E','F'):4,('G','H','I'):5,('J','K','L'):6,('M','N','O'):7,
      ('P','Q','R','S'):8,('T','U','V'):9,('W','X','Y','Z'):10}
target = input()
s=0
for i in target:
    if i in ('A','B','C'):
        s+=3
    elif i in ('D','E','F'):
        s+=4
    elif i in('G','H','I'):
        s+=5
    elif i in ('J','K','L'):
        s+=6
    elif i in ('M','N','O'):
        s +=7
    elif i in ('P','Q','R','S'):
        s +=8
    elif i in ('T','U','V'):
        s += 9
    elif i in ('W','X','Y','Z'):
        s += 10
print(s)

################################
"""
#크로아티아 알파벳

c_alhpa = ['c=','c-','dz=','d-','lj','nj','s=','z=']


target=input()
cnt=len(target)

for i in c_alhpa:
    if target.count(i):
        cnt-=target.count(i)


print(cnt)
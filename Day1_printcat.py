'''
백준
입출력과 사칙연산
고양이
개
A*B
A/B
사칙연산
나머지
곱셈 2588번문제
'''


print('''\    /\\
 )  ( ')
(  /  )
 \(__)|''')


print('''|\_/|
|q p|   /}
( 0 )"""\\
|"^"`    |
||_/=\\\\__|''')

'''
#사칙연산
L = list(map(int, input().split()))

print(L[0]+L[1])
print(L[0]-L[1])
print(L[0]*L[1])
print(int(L[0]/L[1]))
print(L[0]%L[1])

#나머지 
L = list(map(int, input().split()))
print((L[0]+L[1])%L[2])
print((L[0]%L[2]+L[1]%L[2])%L[2])
print((L[0]*L[1])%L[2])
print(((L[0]%L[2])*(L[1]%L[2]))%L[2])
'''

#곱셈문제
a = int(input())
b =  int(input())
print((b%10)*a)
print(int(b%100*0.1)*a)
print(int(b*0.01)*a)
print(a*b)
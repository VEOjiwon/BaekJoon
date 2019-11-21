"""
백준
if문 문제

"""
"""
#1번(1330번) 두 수 비교하기
a = list(map(int, input().split()))

if a[0]>a[1] :
    print(">")
elif a[0]<a[1] :
    print("<")
else :
    print("==")


#2번(9498번)
score = int(input())

if 90 <= score <= 100 :
    print("A")
elif 80 <= score <90:
    print("B")
elif 70 <= score < 80:
    print("C")
elif 60 <= score < 70:
    print("D")
else:
    print("F")


#3번(27533번) 윤년
year = int(input())

if (year%4==0 and year%100!=0) or year%400 == 0:
    print(1)
else:
    print(0)
"""

#4번(2884번) 알람시계
h, m = input().split()
h = int(h)
m = int(m)

if m-45<0:
    if h-1<0:
        sh=23
        sm=m+15
    else :
        sh=h-1
        sm=m+15
else:
    sh=h
    sm=m-45

print(sh, sm)
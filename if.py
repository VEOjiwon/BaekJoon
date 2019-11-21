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

"""
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

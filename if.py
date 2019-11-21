"""
백준
if문 문제

"""

#1번(1330번) 두 수 비교하기
a = list(map(int, input().split()))

if a[0]>a[1] :
    print(">")
elif a[0]<a[1] :
    print("<")
else :
    print("==")
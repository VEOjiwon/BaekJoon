"""
백준
코드스니핑용 공간
"""

#1 12 와 같은 입력을 받는 코드
L = list(map(int, input().split()))

#띄어쓰기로 구분된 한줄의 여러입력 받고 int로 형 변환 (처음에 받을 때는 str임)
a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)

#시간절약을 위한 인풋코드
import sys

# 2 4 5 같은 입력 한줄에 받기 str타입임
sys.stdin.readline()

sys.stdin.readline().rstrip()  # \n문자제거해줌

# 2 4 5 같은 입력 한줄에 받아서 띄어쓰기 단위로 리스트에 집어넣기
L = list(map(int,sys.stdin.readline().rstrip().split()))

#print , sep 옵션 (기본 -> 공백)
print("Case #",":",L[0]+L[1],sep="")

#별찍기 기본
count = int(input())

for i in range(0,count):
    print("*"*(i+1)) #이 포맷팅 참고할 것
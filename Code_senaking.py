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

#프린트 옵션
print(" "*tmp,end='',sep="")    #end =''은 \n 없애주는 용

#for문 옵션
for i in range(10,0,-1)           #10부터 0까지 빼가면서 계산하겠다는 용

#if문 옵션
if not l:         #l(list)가 비었는지 안비었는지 검사하는 용
if seq:           #이거도 사용가능

###################################

#여러줄에 걸친 input 받는 법, 단 엔터 한번 더 입력해야 끝낼 수 있음
from pip._vendor.distlib.compat import raw_input
l = list()
while True:
    input_data = raw_input()
    if input_data == '':
        break
    else:
        l.append(input_data)
print(l)

#나누기 관련
exxx = 13 // 4 # exxx= 3 이다.. 소수점 이하를 버려준다
exxx2 = divmod(9,5) # exxx2 = (1,4)이다. 몫과 나머지 둘 다 구해준다.


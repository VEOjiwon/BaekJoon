"""
1 차원 배열
"""

#최대 최소값
import sys
length = int(sys.stdin.readline())
l = list(map(int,sys.stdin.readline().rstrip().split()))
max = -1000000
min = 1000000
for i in l:
    if max<=i:
        max=i
    if min>=i:
        min=i

print(min,max)
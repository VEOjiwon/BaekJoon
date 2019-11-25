"""
while문
"""


"""
#A + B - 5
import sys
while True:
    l=list(map(int,sys.stdin.readline().rstrip().split()))
    if l[0] and l[1] !=0 :
        print(l[0]+l[1])
        continue
    else:
        break
###############################################
"""
# A+B - 4
import sys
while True:
    l=list(map(int,sys.stdin.readline().rstrip().split()))
    if not l:
        break
    print(l[0]+l[1])




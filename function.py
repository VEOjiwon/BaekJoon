"""
백준 함숩부분


#정수 n개의 합
def solve(a:list) -> int :
    result = 0
    for i in a:
        result+=i
    return result
######################################
#이거도 되다니
solve = sum



######################################3
#셀프 넘버


l=[]
sums = 0
for i in range(1,10000):
    l.append(i)

for i in range(1,10000):
    sums=i
    for j in str(i):
        sums=sums+int(j)
    try:
        l.remove(int(sums))
    except ValueError as e:
        pass


for i in l:
    print(i)
######################################3
"""

#한수

def isnt_han(target):
    a=[]
    for i in str(target):
        a.append(int(i))
    if len(a)==1:
        return 1 #1자리수
    tmp = a[1] - a[0]
    for i in range(0,len(a)-1):
        if a[i+1]-a[i] != tmp :
            return 0
    return 1


target =int(input())
cnt = 0


for i in range(1,target+1):
    cnt+=isnt_han(i)
print(cnt)
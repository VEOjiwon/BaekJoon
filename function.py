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
"""
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
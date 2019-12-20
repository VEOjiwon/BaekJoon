#find prime
n = int(input())
l = list(map(int, input().split()))
cnt = n
for i in l:
    if i==1:
        cnt-=1
        continue
    for k in range(2,i):
        if(i%k==0):
            cnt-=1
            break
print(cnt)

#prime problem #2581
def is_prime(i):
    if i==1:
        return 0
    for k in range(2,i):
        if(i%k==0):
            return 0
            break
    return 1

m = int(input())
n = int(input())

l = []
for i in range(m,n+1):
    if is_prime(i):
        l.append(i)
if len(l) == 0:
    print('-1')
else:
    print(sum(l))
    print(min(l))

######################################################################
#실패함.. 다시
"""
def is_prime(i):
    if i==1:
        return 0
    for k in range(2,i):
        if(i%k==0):
            return 0

    return 1
"""
m, n = input().split()

m = int(m)
n = int(n)

# l = []
cnt = 1
for i in range(m, n + 1):
    if i == 1:
        continue
    for k in range(2, i):
        if (i % k == 0):
            break
    if k == i - 1:
        print(i)



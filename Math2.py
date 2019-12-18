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
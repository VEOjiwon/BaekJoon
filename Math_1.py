#Break event point

a,b,c = map(int,input().split())

k=c-b
if b<c:
    cnt=int(a/k+1)
    print(cnt)
else:print("-1")
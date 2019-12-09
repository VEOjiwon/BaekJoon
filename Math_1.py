#Break event point

a,b,c = map(int,input().split())

k=c-b
if b<c:
    cnt=int(a/k+1)
    print(cnt)
else:print("-1")

#sugar delivery
target = int(input())

m5 = target//5
mod5 = target % 5
cnt=0

cant = [4,7]
if target in cant:
    cnt = -1
else :
    if mod5 == 0:
        cnt = m5
    elif  (mod5 ==1) or (mod5==4) :
        tmp = m5-1
        tmp3 = target-(5*tmp)
        cnt=tmp3//3+tmp
    elif mod5 == 2 :
        tmp = m5-2
        tmp3 = target-(5*tmp)
        cnt=tmp3//3+tmp
    elif mod5 ==3:
        cnt = mod5//3 + m5

print(cnt)
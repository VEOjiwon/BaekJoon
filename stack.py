import sys

# stack

sta=[]
def push(x):
    global sta
    sta.append(x)

def pop():
    global sta
    if len(sta)==0:
        return -1
    else:
        return sta.pop()
def size():
    global sta
    return len(sta)

def empty():
    global sta
    if len(sta)==0:
        return 1
    else: return 0

def top():
    global sta
    if len(sta)==0: return -1
    else : return sta[-1]



rept = int(input())

for i in range(rept):
    tar = sys.stdin.readline().split()
    if tar[0]=="push":
        push(tar[1])
    elif tar[0]=="pop":
        print(pop())
    elif tar[0]=="size":
        print(size())
    if tar[0]=="empty":
        print(empty())
    if tar[0]=="top":
        print(top())
# indian_poker
import random


# 컴퓨터 배팅시스템 알고리즘
def opbet_system(mybet, me, opcoin):
    return


# 가위바위보로 선 정하는 코드
def int_to_ro(a):
    if a == 1:
        return "rock"
    elif a == 2:
        return "Scissors"
    else:
        return "Papper"


print("welecome to the indian poker game!!")
print("we have to decide the order")
while True:
    print("insert 1(rock) or 2(Scissors) or 3(Papper)")
    print("------------------------------------------")
    m = int(input())
    o = random.randrange(1, 4)
    if m == o:
        print("you:", int_to_ro(m))
        print("opponent:", int_to_ro(o))
        print("same thing")
        continue
    elif (m == 1 and o == 2) or (m == 2 and o == 3) or (m == 3 and o == 1):
        print("you:", int_to_ro(m))
        print("opponent:", int_to_ro(o))
        print("you win!!!")
        who_first = 0
        break
    else:
        print("you:", int_to_ro(m))
        print("opponent:", int_to_ro(o))
        print("you lose!!!")
        who_first = 1
        break

print("------------------------------------------")

# 덱 생성
d1 = [card for card in range(1, 11)]
d2 = [card for card in range(1, 11)]
deck = d1 + d2

who_first = 0  # 0은 내가 선 1은 상대가 선

# 게임진행
op = deck.pop(random.randrange(0, len(deck) - 1))
me = deck.pop(random.randrange(0, len(deck) - 1))

mycoin = 30
opcoin = 30
total_bat = 0
mybet = 0
opbet = 0

# 기본배팅
print("stake is 1")
mycoin -= 1
opcoin -= 1
total_bat += 2
print("total batting is ", total_bat)

print("my coin is : ", mycoin)
print("opponent's coin is : ", opcoin)

print("------------------------------------------")
print("this is Opponent's number")
print(op)
print("------------------------------------------")

if who_first == 0:
    print("you are first turn")
    print("insert your bet number")
    mybet = mybet + int(input())
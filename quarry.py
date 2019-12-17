# 수열과 커리 1


size_array = int(input())
quarry = list(map(int, input().split()))
quarry_num = int(input())

tar = []
for i in range(0, quarry_num):
    tar.append(input())

for t in tar:
    cnt = 0
    # start = int(t.split()[0])
    # end = int(t.split()[1])
    # compare = int(t.split()[2])
    for i in range(int(t.split()[0]), int(t.split()[1])):
        if int(t.split()[2]) <= quarry[i]:
            cnt += 1
    print(cnt)

"""
시간초과로 실패함
트리 이용해야 하지만 기억이 안나므로
알고리즘 및 자료구조 공부 후 다시 풀어봐야겠음
"""
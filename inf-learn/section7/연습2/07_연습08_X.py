
##### 사과나무(BFS)
from collections import deque

def solution():
    global  Sum
    answer = 0
    print(ch)

    qu = deque()

    mid = N//2
    qu.append((mid, mid))
    ch[mid][mid] =1
    Sum += inp[mid][mid]

    L = 0
    while True :
        if L == mid :
            break
        else:
            size = len(qu)
            for i in range(size):
                now = qu.popleft()
                for j in range(4):
                    if ch[now[0] + dx[j]][now[1] +dy[j]] == 0:
                        ch[now[0] + dx[j]][now[1] + dy[j]] = 1
                        qu.append((now[0] + dx[j],now[1] + dy[j] ))
                        Sum += inp[now[0] + dx[j]][now[1] + dy[j]]

        L += 1
    #print(ch)
    for c in ch:
        print(c)
    print(Sum)
    return answer

N = 5

inp = [
    [10,13,10,12,15],
    [12,39,30,23,11],
    [11,25,50,53,15],
    [19,27,29,37,27],
    [19,13,30,13,19]
]

ch = [[0] * N for _ in range(N)]
dx = [0, 1, 0, -1]  # 시계 방향 ..
dy = [-1, 0, 1, 0]

Sum = 0

re = solution()
print(re)
#=>
print('====================')

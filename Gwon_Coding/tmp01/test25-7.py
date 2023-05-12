
#
from collections import deque

data = [[0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 0, 0, 0, 1, 0],
        [1, 1, 1, 0, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 1, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]]

# BFS 는 스택으로 구현한 DFS 와 동일,
# 상하좌우 를 살핀다
# 육지 0
ans = 0

def find_0():
    for i in range(len(data)):
        for j in range(len(data[0])):
            print(data[i][j])
            if data[i][j] == 0 :  # 처음 발견된 0
                return i, j
    return -1, -1  # 0 이 없으면 이리로 옴

d_x = [-1,1,0,0]
d_y = [0,0,-1,1]

def dfs(x, y) :
    data[x][y] =1
    for i in range(4):
        nx = x + d_x[i]
        ny = y + d_y[i]
        if 0 <= nx < len(data) and 0 <= ny < len(data[0]):
            if data[nx][ny] == 0 :
                dfs(nx, ny)

# ti, tj = find_0()
# print(ti, tj)
# dfs(ti, tj)

while True :
    ti, tj = find_0()
    if ti == -1 :
        break
    print(ti, tj)
    ans += 1
    dfs(ti, tj)
    #ans += 1

print(ans)


'''
코드를 구현하다 보면,
→ ← ↑ ↓ 이렇게 네 방향으로 진행해야 할 때가 있다. 이런 경우, x값을 증감하는지, y값을 증감하는지 간혹 헷갈릴 때가 있다.

ar[0][0]	ar[0][1]	ar[0][2]
ar[1][0]	ar[1][1]	ar[1][2]
ar[2][0]	ar[2][1]	ar[2][2]

이렇게 간단한 3X3정도 이차원 배열을 그려서 확인하는 게 편하다.
→ : y값을 증가시키면 된다.
← : y값을 감소시키면 된다.
↑ : x값을 감소시키면 된다.
↓ : x값을 증가시키면 된다.

x,y의 증감을 판단할 때, x축, y축의 그래프를 생각하면, 오히려 잘못 생각할 수 있으므로, 이렇게 간단한 이차원 배열을 그려보는 게 좋다.


[비슷한 고민을 하는구먼]
https://m.blog.naver.com/PostView.nhn?isHttpsRedirect=true&blogId=chocolate318&logNo=221379957992&categoryNo=6&proxyReferer=

'''


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

def bfs(x, y):  # ti, tj
    global ans
    # 상하좌우를 살펴야됨
    d_x = [-1, 1, 0, 0]
    d_y = [0, 0, -1, 1]

    qu = deque()
    # 처음 넘어온 값 넣어준다
    qu.append([x, y])

    while len(qu) >0 :
        tx, ty = qu.popleft()
        # 뺐을 때 1로 셋팅 (이래도 될 거 같은데)
        data[tx][ty] = 1

        for i in range(4):  # 4 방향이니
            if 0 <= tx + d_x[i] < len(data) and data[tx + d_x[i]][ty] == 0:
                qu.append([tx + d_x[i] , ty] )
            if 0 <= ty + d_y[i] < len(data[0]) and data[tx][ty + d_y[i]] == 0:
                qu.append([tx , ty + d_y[i]])
        print(qu)
    ans += 1

# ti, tj = find_0()
# print(ti, tj)
# bfs(ti, tj)

while True :
    ti, tj = find_0()
    if ti == -1 :
        break
    print(ti, tj)
    bfs(ti, tj)

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


##### 토마토(BFS 활용)

from collections import deque

def solution():
    answer = 0
    qu = deque()
    for i in range(M):
        for j in range(N):
            if inp[i][j] == 1:
                qu.append((i,j))

    while qu:
        now = qu.popleft()
        x = now[0]
        y = now[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 경계선을 넘지 않도록.. + 안 익은 토마토(0)
            if 0 <= nx < M and 0 <= ny < N and ch[nx][ny] == 0 :
                ch[nx][ny] = ch[x][y] +1
                inp[nx][ny]= 1 # 익은 것으로...
                qu.append((nx, ny))

    # 확인
    for c in ch :
        print(c)
    # 여긴 loop 좀 돌아야...
    flag = 1
    rtn = 0
    for i in range(M):
        for j in range(N):
            if inp[i][j] == 0:
                flag = 0
    if flag ==1 :
        for i in range(M):
            for j in range(N):
                if ch[i][j] > rtn:
                    rtn = ch[i][j]
        print(rtn)
    else:
        print(-1)

    return answer

N = 6  # M은 상자의 가로 칸의 수,
M = 4  # N은 상자의 세로 칸의 수를

inp = [
    [0, 0, -1, 0, 0, 0],
    [0, 0, 1, 0, -1, 0],
    [0, 0, -1, 0, 0, 0],
    [0, 0, 0, 0, -1, 1]
]
# (방문기록 대신) 거리
ch = [[0]*N for _ in range(M)]

dx = [ -1, 0, 1, 0]  # 시계 방향으로
dy = [0, 1, 0, -1]

cnt = 0

re = solution()
print(re)
#=>
print('====================')

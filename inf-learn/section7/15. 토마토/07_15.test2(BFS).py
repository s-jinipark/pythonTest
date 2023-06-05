
# BFS
from collections import deque

def solution():
    answer = 0
    qu = deque()
    cnt = 0
    for i in range(N):
        for j in range(M):
            if inp[i][j] == 1 : # 익은 토마토 1
                qu.append((i,j))
                while qu :
                    now = qu.popleft()
                    inp[now[0]][now[1]] = 1
                    for k in range(4):
                        #next
                        nx = now[0] + dx[k]
                        ny = now[1] + dy[k]
                        if 0 <= nx < N and 0 <= ny < M :
                            if inp[nx][ny] == 0 and inp[nx][ny] != -1 :
                                qu.append((nx,ny))
        cnt += 1  # cnt 의 위치 중요(**)
    print('cnt:', cnt)
    return answer

M = 6  # 가로 칸수
N = 4  # 세로 칸수
inp = [
    [0, 0, -1, 0, 0, 0],
    [0, 0, 1, 0, -1, 0],
    [0, 0, -1, 0, 0, 0],
    [0, 0, 0, 0, -1, 1]
]

visted = [[0]*N for _ in range(N)]
print(visted)
dx = [-1,1,0,0]  # 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 네 방향
dy = [0,0,-1,1]


re = solution()

print('re :', re)
#=>
print('==============================')


import sys
from collections import deque

'''
미로 탐색
'''
sys.stdin = open("input15-2-1.txt", "rt")
N, M = map(int, input().split())
print(N, M)

maze = [list(map(int, input())) for _ in range(N)]
print(maze)

d = [(-1,0), (1,0), (0,-1), (0,1)]  # 상하 좌우
# 수학의 x, y 라기 보다는 , 행렬의 x, y 로
ddx = [-1, 1, 0 , 0]
ddy = [0, 0, -1, 1]
# -> 난 이거 쓸래

q = deque()
q.append((0,0))

def bfs():
    while q :
        x, y = q.popleft()
        for k in range(len(ddx)):
            dx = x + ddx[k]
            dy = y + ddy[k]
            if 0 <= dx < N and 0 <= dy < M :
                if maze[dx][dy] == 1 :
                    maze[dx][dy] = maze[x][y] + 1
                    q.append((dx, dy))

maze[0][0] = 1
bfs()
print(maze[N-1][M-1])

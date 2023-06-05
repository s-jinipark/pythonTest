
# BFS , 최단거리
from collections import deque

def solution():
    answer = 0
    qu = deque()
    start = 0
    end = 6
    qu.append((start, start))
    visted[start][start] = 0
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while qu:
        now = qu.popleft()
        print(now, visted[now[0]][now[1]])
        if now[0]== N-1 and now[1]== N-1 :
            break
        for i in range(4):
            next_x = now[0] + dx[i]
            next_y = now[1] + dy[i]
            if 0<=next_x<N  and 0<=next_y<N:  # 판을 벗어나면 안되고
                if inp[next_x][next_y] == 0 : # 벽이면 안되고
                    if visted[next_x][next_y] == 0:
                        qu.append((next_x,next_y))
                        visted[next_x][next_y] = visted[now[0]][now[1]] +1

    return answer


N = 7  # 문제에 7 X 7 이라고..
inp = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [1, 1, 0, 1, 0, 1, 1],
    [1, 1, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 0]
]
visted = [[0]*N for _ in range(N)]
print(visted)

re = solution()
print('re :', re)
#=>
print('==============================')

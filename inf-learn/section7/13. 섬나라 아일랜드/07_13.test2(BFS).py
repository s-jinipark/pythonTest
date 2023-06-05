
# BFS
from collections import  deque

def solution():
    global  cnt
    answer = 0
    qu = deque()

    # 시작점을 찾은 뒤 DFS 부른다
    for i in range(N):
        for j in range(N):
            if inp[i][j] == 1 :
                qu.append((i,j))
                while qu:
                    now = qu.popleft()
                    inp[now[0]][now[1]]=0
                    for k in range(8):
                        next_x = now[0] + dx[k]
                        next_y = now[1] + dy[k]
                        if 0<= next_x < N and 0<= next_y < N :
                            if inp[next_x][next_y] == 1:
                                qu.append((next_x,next_y))

                cnt += 1  # 끝난 뒤 +1 해줌

    return answer

N = 7
inp = [
    [1, 1, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 1],
    [1, 1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 1, 0, 0]
]

visted = [[0]*N for _ in range(N)]
print(visted)
#dx = [-1,1,0,0]
#dy = [0,0,-1,1]
#dx = [-1,-1, 0, 1, 1, 1, 0,-1] # 8방향 - 이것도 엄청 헷갈림
#dy = [ 0, 1, 1, 1, 0,-1,-1,-1]
# 상하 좌우에다 추가로 X 를 그려 보면 (이게 낫다)
dx = [-1, 1, 0, 0, -1, 1, 1,-1]
dy = [0, 0, -1, 1,  1, 1,-1,-1]

cnt = 0

re = solution()
print('cnt', cnt)
print('re :', re)
#=>
print('==============================')

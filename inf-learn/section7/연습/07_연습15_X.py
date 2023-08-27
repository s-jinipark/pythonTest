
##### 토마토(BFS 활용)

from collections import deque

def findFirst1():
    for i in range(M):  # 헷갈리네.
        for j in range(N):
            if inp[i][j]==1:
                return(i,j)
    return(-1,-1)

def solution():
    answer = 0

    '''
    이건 '플러드 필' 인가?
    
    정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 
    정수 -1은 토마토가 들어있지 않은 칸
    
    이것도 최초 1을 찿아서 BFS 하고
    루핑 돌면서 끝낸다.
    '''

    # 모두 익은 상태인지는 여기서 체크해야 할 듯

    fst = findFirst1()
    print(fst)
    cnt = 1
    qu = deque()
    ch[fst[0]][fst[1]] = 1  # cnt
    qu.append((fst[0],fst[1]))

    while qu:
        now = qu.popleft()
        x = now[0]
        y = now[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and ch[nx][ny] == 0 and inp[nx][ny] == 0:
                ch[nx][ny] = ch[x][y] +1
                inp[nx][ny]= 1 # 익은 것으로...
                qu.append((nx, ny))
        cnt += 1

    # 확인
    for c in ch :
        print(c)
    # for i in inp :
    #     print(i)
    answer = cnt
    return answer

N = 6  # M은 상자의 가로 칸의 수,
M = 4  # N은 상자의 세로 칸의 수를

inp = [
    [0, 0, -1, 0, 0, 0],
    [0, 0, 1, 0, -1, 0],
    [0, 0, -1, 0, 0, 0],
    [0, 0, 0, 0, -1, 1]
]
#방문기록
ch = [[0]*N for _ in range(M)]

dx = [ -1, 0, 1, 0]  # 시계 방향으로
dy = [0, 1, 0, -1]

cnt = 0

re = solution()
print(re)
#=>
print('====================')

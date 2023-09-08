
##### 미로탐색(DFS)

def DFS(x, y):
    #print(x,y)
    global  cnt
    if x == N-1 and y == N-1:
        print(x,y)
        cnt +=1
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < N and 0 <= ny < N  and inp[nx][ny] == 0 and ch[nx][ny] == 0:
                ch[nx][ny] = 1
                DFS(nx, ny)
                ch[nx][ny] = 0   # 웁스 갔다 왔으면 0 으로 다시 셋팅

def solution():
    answer = 0

    '''
    미로를 탈출하는 경로의 가지수를 출력
    
    최단경로가 아니고 가지 수 니까 DFS
    (다 해보는 거)
    '''
    ch[0][0] = 1
    DFS(0,0)
    print('cnt' , cnt)
    return answer

N = 7

inp = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [1, 1, 0, 1, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0]
]
#방문기록
ch = [[0]*N for _ in range(N)]

dx = [ -1, 0, 1, 0]  # 시계 방향으로
dy = [0, 1, 0, -1]

cnt = 0

re = solution()
print(re)
#=> 8
print('====================')

inp = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 0]
]
#방문기록
ch = [[0]*N for _ in range(N)]

dx = [ -1, 0, 1, 0]  # 시계 방향으로
dy = [0, 1, 0, -1]

cnt = 0

re2 = solution()
print(re2)
#=> 24
print('====================')


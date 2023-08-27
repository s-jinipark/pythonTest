
##### 사다리 타기(DFS)

def DFS(x, y):

    if x == 0:
        print(x, y)
    else :
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < N and 0<= ny < N :  # 범위를 벗어나면 안되고..
                if inp[nx][ny] == 1 and ch[nx][ny] == 0 :
                    print(nx, ny)
                    ch[nx][ny] = 1
                    DFS(nx, ny)
                    break

def solution():
    answer = 0

    '''
    2를 찾은 다음에 x 가 0 일때까지 위로 올라간다
    올라가다가 옆으로 갈 수 있으면 간다
    '''
    end = ''
    # 2를 찾아
    for i in range(N):
        if inp[9][i] == 2 :
            end = (9, i)
    print(end)

    ch[end[0]][end[1]] = 1
    DFS(end[0], end[1])

    return answer

N = 10

inp = [
    [1, 0, 1, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 2, 0, 1, 0, 1]
]

ch = [[0]*N for _ in range(N)]
dx = [ 0, 0,  -1]  # 시계 방향으로 -> (아래 방향은 빼고 , 위로 올라가는거를 뒤로)
dy = [-1, 1,   0]

cnt = 0

re = solution()
print(re)
#=>
print('====================')

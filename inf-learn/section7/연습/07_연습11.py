
##### 등산경로(DFS)

def DFS(x, y):
    global  cnt
    if inp[x][y] == Max :
        print(x, y)
        cnt +=1
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < N and 0<= ny < N and inp[nx][ny] > inp[x][y] and ch[nx][ny] == 0 :
                ch[nx][ny] = 1
                DFS(nx,  ny)
                ch[nx][ny] = 0

def solution():
    answer = 0

    '''
    등산을 할 때는 그 구역의 위, 아래, 왼쪽, 오른쪽 중 
    더 높은 구역으로만 이동
    
    등산 경로 몇가지 ??
    '''
    ch[MinX][MinY] = 1
    DFS(MinX, MinY)

    return answer

# N = 5
#
# inp = [
#     [2, 23, 92, 78, 93],
#     [59, 50, 48, 90, 80],
#     [30, 53, 70, 75, 96],
#     [94, 91, 82, 89, 93],
#     [97, 98, 95, 96, 100]
# ]

N = 6

inp = [
    [2, 23, 92, 78, 93, 100],
    [59, 50, 48, 90, 80, 101],
    [30, 53, 70, 75, 96, 102],
    [94, 91, 82, 89, 93, 103],
    [97, 98, 95, 96, 100, 104],
    [102, 103, 104, 105, 106, 107]
]

#방문기록
ch = [[0]*N for _ in range(N)]

dx = [ -1, 0, 1, 0]  # 시계 방향으로
dy = [0, 1, 0, -1]

cnt = 0

# 출발점 get
Min = 2147000000
Max = 0
MinX = 0
MinY = 0
for i in range(N):
    for j in range(N):
        if inp[i][j] < Min:
            Min = inp[i][j]
            MinX = i
            MinY = j
        if inp[i][j] > Max:
            Max = inp[i][j]
print(Min, Max)

re = solution()
print(cnt)  #print(re)
#=>
print('====================')

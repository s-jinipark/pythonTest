
# DFS , 이경우 가지수를 출력해야 해서.... [최단거리 아님]

def DFS(x, y) :
    #if x == N-1 and y == N-1 : # 종료 조건
    if x == 6 and y == 6:  # 종료 조건
        print(inp)
        return
    else:
        # 상하좌우
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]

            if 0<= next_x<N and 0<= next_y<N : # 범위를 벗어 났는지 체크
                if inp[next_x][next_y] == 0:
                    inp[next_x][next_y]=1
                    DFS(next_x, next_y)
                    inp[next_x][next_y] = 0

                ##### 1st  ->  visited 를 따로 했더니 무한 루프... ???
                # if visted[next_x][next_y] == 0:
                #     visted[next_x][next_y]=1
                #     DFS(next_x, next_y)
                #     visted[next_x][next_y] = 0

def solution():
    answer = 0

    #visted[0][0]=1
    inp[0][0]=1
    DFS(0,0)

    return answer


N = 7  # 문제에 7 X 7 이라고..
inp = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [1, 1, 0, 1, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0]
]
visted = [[0]*N for _ in range(N)]
print(visted)
dx = [-1,1,0,0]
dy = [0,0,-1,1]
re = solution()
print('re :', re)
#=>
print('==============================')

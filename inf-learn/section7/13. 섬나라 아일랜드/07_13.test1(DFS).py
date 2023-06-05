
# DFS
def DFS(x, y):
    # 종료 조건이 딱히 없음
    inp[x][y] =0
    for i in range(8):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if 0<= next_x < N and 0<= next_y < N : # 범위 체크
            if inp[next_x][next_y] == 1 :
                DFS(next_x,next_y)
    # 1st 에서 6 이 나옴 (답은 5) ???
    # 대각선을 포함해야 한다는 사실 간과

def solution():
    global  cnt
    answer = 0

    # 시작점을 찾은 뒤 DFS 부른다
    for i in range(N):
        for j in range(N):
            if inp[i][j] == 1 :
                #inp[i][j]=0
                DFS(i, j)
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

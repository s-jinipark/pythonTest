
# DFS
def DFS(x, y):
    global  cnt
    # 종료 조건 없이...
    cnt += 1
    inp[x][y] = 0  # 0 으로 바꿔버림.
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if 0 <= next_x < N and 0 <= next_y < N :  # 범위 체크
            if inp[next_x][next_y] == 1:
                DFS(next_x,next_y)

def solution():
    global  cnt
    answer = 0
    res = []

    # 시작점을 찾은 뒤 부른다
    for i in range(N):
        for j in range(N):
            if inp[i][j] == 1 :
                cnt = 0
                DFS(i,j)
                res.append(cnt)  # 끝난 뒤 적재

    res.sort()
    print('res', res)
    return answer

N = 7
inp = [
    [0, 1, 1, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 1, 1],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 0, 0, 0]
]

visted = [[0]*N for _ in range(N)]
print(visted)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

cnt = 0

re = solution()
print('cnt', cnt)
print('re :', re)
#=>
print('==============================')

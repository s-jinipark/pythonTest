
# import sys
# sys.setrecursionlimit(10**6)

# 관계 없음 DFS, BFS
# 격자판 탐색 - 영역의 넓이 찾거나 하는거(단지번호, 섬나라)

def DFS(x, y, h, visited):
    visited[x][y] == 1
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if 0<= next_x < N and 0<= next_y < N:
            #if inp[next_x][next_y]> h:
            if visited[next_x][next_y] == 0 and inp[next_x][next_y] > h:
                DFS(next_x,next_y, h, visited)

def solution():
    global  cnt
    answer = 0
    # 문제에 '높이는 1이상 100 이하의 정수이다.' 라고 있어서
    for h in range(100): # 이경우 100번 돈다
        visited = [[0] * N for _ in range(N)]
        cnt =0
        for i in range(N):
            for j in range(N):  # 이제서야 이중 for 문
                if inp[i][j]>h and visited[i][j] == 0:
                    cnt += 1
                    DFS(i, j, h, visited)
        if cnt ==0:
            break
    return answer

N = 5
inp = [
    [6, 8, 2, 6, 2],
    [3, 2, 3, 4, 6],
    [6, 7, 3, 3, 2],
    [7, 2, 5, 3, 6],
    [8, 9, 5, 2, 7]
]

# visited = [[0]*N for _ in range(N)]
# print(visited)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

cnt = 0

re = solution()
print('cnt', cnt)
print('re :', re)
#=>
print('==============================')
'''
오류 남
RecursionError: maximum recursion depth exceeded in comparison
'''
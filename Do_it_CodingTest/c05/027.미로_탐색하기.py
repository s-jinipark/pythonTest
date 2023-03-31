
import sys
from collections import  deque

sys.stdin = open("input_c05-027.txt", "rt")

n, m = map(int, input().split())   # n X m 크기의 배열로 표현되는 미로

A = [[0] * m for _ in range(n) ]

visited = [[False] * m for _ in range(n) ]

#####
dx = [0, 0, -1, 1]  # 상하좌우 ?
dy = [1, -1, 0, 0]
#####

def well_print(lst) :
    for i in range(len(lst)):
        print(lst[i])

#print(n, m, A)
print(n, m)
well_print(A)
print('--------------------')
well_print(visited)

print('----- 셋팅 ----------')

for i in range(n):
    numbers = list(input())
    for j in range(m):
        A[i][j] = int(numbers[j])
well_print(A)

'''
완전탐색을 진행하며 몇 번째 깊이에서 원하는 값을 찾을 수 있는지를 구하는 것과 동일
BFS 가 적합한 이유는 해당 깊이에서 갈 수 있는 노드 탐색을 마친 후 다음 깊이로 넘어가기 때문

'''

def BFS(i, j):
    queue = deque()
    queue.append((i,j))
    visited[i][j] = True
    while queue :
        now = queue.popleft()  # now 를 뽑는다.
        for k in range(4):
            x = now[0] + dx[k]
            y = now[1] + dy[k]
            if x >= 0 and y >= 0 and x < n and y < m :  # 좌표 유효성 검사
                if A[x][y] != 0 and not visited[x][y] :
                    visited[x][y] = True
                    A[x][y] = A[now[0]][now[1]] +1
                    queue.append((x,y))

BFS(0, 0)

print('--------------------')

well_print(A)
print(A[n-1][m-1])

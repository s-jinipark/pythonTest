
import sys
from collections import deque

'''
그래프를 DFS 로 탐색한 결과와 BFS 로 탐색한 결과를 출력하는 프로그램을 작성

'''
sys.stdin = open("input15-3-2.txt", "rt")
# 정점의 개수 N, 간선의 개수 M, 탐색 시작 V
N, M, V = map(int, input().split())
print(N, M, V)

vertex =[[0] *(N+1) for i in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    vertex[a][b] = vertex[b][a]=1
visit=[0]*(N+1)

print(vertex, visit)

def dfs(V):
    visit[V] = 1
    print(V, end=' ')
    for i in range(1, N+1):
        if (visit[i]==0 and vertex[V][i]==1):
            dfs(i)

def bfs(V):
    visit[V]=1
    queue = deque()
    queue.append(V)
    while queue:
        V = queue.popleft()
        print(V, end=' ')
        for i in range(1, N+1):
            if (visit[i]==0 and vertex[V][i]==1):
                queue.append(i)
                visit[i] =1

dfs(V)
visit=[0]*(N+1)
print('\n---------------')
bfs(V)
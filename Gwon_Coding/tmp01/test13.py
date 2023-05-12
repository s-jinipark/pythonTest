
from collections import deque
import sys
input = sys.stdin.readline

# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다.
# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
# 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

#N, M, V = map(int, input().split())
#print(N, M, V)
N, M, V = 4,5,1
#N, M, V = 5,3,1

graph = [[] for _ in range(N+1)]

# for _ in range(M):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

graph = [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]]

print(graph)

for i in range(1, len(graph)):
    graph[i].sort()

visited = [0] * (N+1)
count = 1
def dfs(n):
    global count
    visited[n] = count
    print(n, end=' ')
    graph[n].sort()  # 번호 작은 거 먼저 방문
    for i in graph[n]:
        #print(i)
        if visited[i] == 0 :
            count += 1
            dfs(i)

def bfs(n):
    global count
    visited[n] = 1
    print(n, end=' ')
    qu = deque([n])  # 맨처음 n
    while qu :
        tmp = qu.popleft()  # 바로 뽑는다
        graph[tmp].sort()
        for i in graph[tmp]:
            if visited[i] == 0 :
                print(i, end=' ')
                qu.append(i)
                count += 1
                visited[i] = count

dfs(V)
#print(visited)
# for i in range(1, len(visited)):
#     if visited[i] != 0 :
#         print(visited[i], end=' ')
print()
count = 1
visited = [0] * (N+1)

bfs(V)
print()
# for i in range(1, len(visited)):
#     if visited[i] != 0 :
#         print(visited[i], end=' ')

'''
https://www.acmicpc.net/board/view/91929

테스트_03: https://www.acmicpc.net/board/view/83538
5 3 1
1 5
3 5
5 2
[1, 5, 2, 3]
[1, 5, 2, 3]

'''
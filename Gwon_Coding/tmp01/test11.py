
from collections import deque
import sys
input = sys.stdin.readline
# 정점의 수 N (5 ≤ N ≤ 100,000), 간선의 수 M (1 ≤ M ≤ 200,000), 시작 정점 R (1 ≤ R ≤ N)이 주어진다.

n, m, r = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [0] * (n+1)

# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
#
# print(graph)

graph = [[], [4, 2], [1, 3, 4], [2, 4], [1, 2, 3], []]
#print(graph)
count = 1

def bfs(n):
    global count
    qu = deque()
    qu.append(n)
    visited[n] = count  # 첫번째 처리
    count += 1  # count 올림
    while len(qu) > 0 :
        tmp = qu.popleft()  # 빼내기 시작
        graph[tmp].sort(reverse=True)
        for i in graph[tmp]:
            if visited[i] == 0 :  # 방문을 안했어..
                visited[i] = count
                count += 1
                qu.append(i)

bfs(r)
print(visited)
for i in range(1, len(visited)):
    print(visited[i])
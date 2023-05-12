
from collections import deque

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

    #qu = []
    qu = deque([r])
    qu.append(n)
    visited[n] = count  # 첫 방문 표시
    count += 1

    while len(qu) > 0  :
        #tmp = qu.pop(0)
        tmp = qu.popleft()
        #visited[tmp] = count
        #count += 1
        #print(tmp)
        graph[tmp].sort()
        for i in graph[tmp]:
            #print(graph[tmp])
            if visited[i] == 0 :
                qu.append(i)
                visited[i] = count
                count += 1

bfs(r)

#print(visited)
for i in range(1, len(visited)):
    print(visited[i])

# 1차로 해본 거
# def bfs(n):
#     global count
#     qu = []
#     qu.append(n)
#     visited[n] = count  # 처음 들어 왔을 때
#     while len(qu) > 0 :
#         count += 1
#         tmp = qu.pop(0)
#         visited[tmp] = count
#         #tmp.sort()
#         print(tmp)
#         for i in graph[tmp]:
#             if visited[i] == 0 : # 방문 안 했으면
#                 qu.append(i)
# bfs(r)
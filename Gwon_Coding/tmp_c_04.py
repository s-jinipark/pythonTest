
# 정점의 수 N , 간선의 수 M , 시작 정점 R
#n, m, r = map(int, input().split())
n, m, r = 5, 5, 1

#arr=[list(map(int, input().split())) for _ in range(n)]

graph = [[]*(n+1) for _ in range(n+1)]
#print(graph)
visited = [0] * (n+1)

arr = [[1, 4], [1, 2], [2, 3], [2, 4], [3, 4]]
for i in range(m):
    #a, b = map(int, sys.stdin.readline().split())
    a, b = arr[i][0], arr[i][1]
    graph[a].append(b)
    graph[b].append(a)
#graph.sort()
print(graph)
# graph 만드는 법..
# 이건 어디 있다 나오는 것인가?

def dfs( n):
    global cnt
    cnt += 1
    visited[n] = cnt
    #print(n)
    graph[n].sort()  # 우와.! 이거 넣었더니 순서대로 됨
    # for i in range(len(graph[n])):
    #     #print(graph[n][i])
    #     if visited[ graph[n][i] ] == 0 :
    #         dfs( graph[n][i])
    for g in graph[n]:
        if visited[g] == 0 :
            dfs(g)
cnt = 0
dfs( 1)

#print(visited)
for i in range(1, len(visited)) :
    print(visited[i])
'''
dfs(V, E, R) {  # V : 정점 집합, E : 간선 집합, R : 시작 정점
    visited[R] <- YES;  # 시작 정점 R을 방문 했다고 표시한다.
    for each x ∈ E(R)  # E(R) : 정점 R의 인접 정점 집합.(정점 번호를 오름차순으로 방문한다)
        if (visited[x] = NO) then dfs(V, E, x);
}

인터넷 검색한 것 -->>

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
count = 1

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    global count
    visited[v] = count
    graph[v].sort()
    for g in graph[v]:
        if visited[g] == 0:
            count += 1
            dfs(g)

dfs(r)

for i in range(1, n + 1):
    print(visited[i])

'''


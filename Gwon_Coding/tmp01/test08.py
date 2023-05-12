

# 정점의 수 N (5 ≤ N ≤ 100,000), 간선의 수 M (1 ≤ M ≤ 200,000), 시작 정점 R (1 ≤ R ≤ N)이 주어진다.

n, m, r = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]

# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
#
# print(graph)

graph = [[], [4, 2], [1, 3, 4], [2, 4], [1, 2, 3], []]
print(graph)
count = 1

def dfs(n):
    global count
    visited[n] = count
    graph[n].sort()  # 한꺼번에 해도 되고 여기서 해도 되고
    for i in graph[n] :
        #print(i)
        if visited[i] == 0 : # 방문하지 않은 상태
            count += 1  # 카운트를 올려 주고
            dfs(i)

dfs(1)


print(visited)
for i in visited:
    print(i)
'''

dfs(V, E, R) {  # V : 정점 집합, E : 간선 집합, R : 시작 정점
    visited[R] <- YES;  # 시작 정점 R을 방문 했다고 표시한다.
    for each x ∈ E(R)  # E(R) : 정점 R의 인접 정점 집합.(정점 번호를 오름차순으로 방문한다)
        if (visited[x] = NO) then dfs(V, E, x);
}

'''
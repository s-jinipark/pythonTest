

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
print(graph)
count = 1

def dfs(n):
    global count
    visited[n] = count
    graph[n].sort(reverse=True)  # 역으로 정렬
    for i in graph[n] :  # n 에 연결된 간선에 가겠다는 말
        if visited[i] == 0 :
            count += 1
            dfs(i)

dfs(r)

print(visited)
for i in range(1, len(visited)):
    print(visited[i])


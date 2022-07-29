def dfs(graph, n, cnt, visited):
    visited[n] = True
    print(n, " ", end="")

    for i in range(1, cnt+1):
        if graph[n][i] == 1 and visited[i] == False:  # 방문 안 했다면
            dfs(graph, i, cnt, visited)


def makegraph(n, vertex):
    graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(len(vertex)):
        graph[vertex[i][0]][vertex[i][1]] = 1
        graph[vertex[i][1]][vertex[i][0]] = 1

    return graph


vertex = [[1, 2],[1, 7], [2, 8], [7, 8], [7, 3], [7, 5], [8, 6], [5, 6], [5, 3], [3, 4],[4, 6]]
cnt = 8
visited = [False for _ in range(cnt+1)]
graph = makegraph(cnt, vertex)  # 그래프 만듬
dfs(graph, 1, cnt, visited)
print()
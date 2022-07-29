def dfs(graph, n, visited):
    visited[n] = True
    print(n, " ", end="")

    for i in graph[n]:
        if visited[i] == False:     # 아직 방문 안한거 chk
            dfs(graph, i, visited)



graph = [[], [2, 7],[1, 8],[4, 5, 7],[4, 6],[3, 6, 7],[4, 5, 8],[1, 3, 5, 8],[2, 6, 7]]

visited = [False for _ in range(len(graph))]
dfs(graph, 1, visited)
print()                    # 1  2  8  6  4  5  3  7
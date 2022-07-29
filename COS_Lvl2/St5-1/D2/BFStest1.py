def bfs(graph, n, visited):
    qu = []

    qu.append(n)
    visited[n] = True

    while(len(qu) > 0):
        v = qu.pop(0)
        print(v, " ", end="")

        for i in graph[v]:
            if visited[i] == False:
                qu.append(i)
                visited[i] = True



graph = [[], [2, 7],[1, 8],[4, 5, 7],[4, 6],[3, 6, 7],[4, 5, 8],[1, 3, 5, 8],[2, 6, 7]]

visited = [False for _ in range(len(graph))]
bfs(graph, 1, visited)
print()                        # 1  2  7  8  3  5  6  4
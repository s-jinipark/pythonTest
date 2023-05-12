def bfs(graph, n, cnt, visited):
    qu = []

    qu.append(n)
    visited[n] = True

    while(len(qu) > 0):
        v = qu.pop(0)
        print(v, " ", end="")

        for i in range(1, cnt+1):
            if graph[v][i] == 1 and visited[i] == False:
                qu.append(i)
                visited[i] = True

def makegraph(n, vertex):
    graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(len(vertex)):
        graph[vertex[i][0]][vertex[i][1]] = 1
        graph[vertex[i][1]][vertex[i][0]] = 1

    return graph

# '시작-끝' 의 형태
vertex = [[1, 2],[1, 7], [2, 8], [7, 8], [7, 3], [7, 5], [8, 6], [5, 6], [5, 3], [3, 4],[4, 6]]
cnt = 8
visited = [False for _ in range(cnt+1)]
graph = makegraph(cnt, vertex)
print(graph) # 2차원 배열에 적재 (연결이 있으면 1로 표시)
bfs(graph, 1, cnt, visited)
print()                       # 1  2  7  8  3  5  6  4
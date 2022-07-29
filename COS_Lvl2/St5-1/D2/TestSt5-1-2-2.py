
graph = [
    [],
    [2, 7],     # 1
    [1, 8],
    [4, 5, 7],
    [4, 6],
    [3, 6, 7],
    [4, 5, 8],
    [1, 3, 5, 8],
    [2, 6, 7]   # 8
]

# 방문
visited = [False] * 9  # 하나 커야 됨

def bfs(v) :
    # 큐 만들고
    q = []
    q.append(v)
    visited[v] = True

    while len(q) > 0 :
        q.pop()
        tmp = q.pop(0)
        print(tmp, " ", end="")
        for i in graph[v] :
            if not visited[i] :
                bfs(i)

bfs(1)


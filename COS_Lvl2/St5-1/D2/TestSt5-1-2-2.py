
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


# 재차 연습_tmp -->
visited =[False] *9

def bfs(v) :
    q = []
    q.append(v)
    visited[v] = True

    while len(q) > 0 :
        tmp = q.pop(0)
        print(tmp, end=' ')
        for i in graph[tmp] :
            if visited[i] is False :
                q.append(i)
                visited[i] = True

bfs(1)

# //<--


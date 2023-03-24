
graph = [[],
         [2, 7],        # 1 에 연결된 것 (2 와 7 이다)
         [1, 8],        # 2
         [4, 5, 7],
         [4, 6],
         [3, 6, 7],
         [4, 5, 8],
         [1, 3, 5, 8],
         [2, 6, 7]      # 8
         ]

visited = [0] * 9   # 하나 많게


def dfs(m) :
    visited[m] = 1
    print(m)
    for i in graph[m] :
        #print('>', i)
        if visited[i] == 0 :
            dfs(i)
dfs(1)


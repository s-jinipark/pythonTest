
from collections import deque

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


def bfs(m) :
    visited[m] = 1
    print(m)
    qu = deque()
    qu.append(m)  # 일단 m 을 붙임
    while len(qu) > 0 : # 0 보다 큰 동안
        tmp = qu.popleft() # 이 부분이 좀 다른 거임
        for t in graph[tmp]:
            #print('>', t)
            if visited[t] == 0 : # 방문 안 했다면
                visited[t] = 1
                qu.append(t)
                print(t)

bfs(1)


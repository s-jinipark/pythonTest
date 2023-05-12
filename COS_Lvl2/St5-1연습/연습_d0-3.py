from collections import deque

graph = [
    [],     # 0
    [2, 3], # 1  # 노드 1에 연결된 노드들
    [4, 5], # 2
    [6],    # 3
    [2, 5], # 4
    [2, 4], # 5
    [3, 7], # 6
    [6]     # 7
]
# 그림 '(0-5)그래프_샘플' 참조

# 방문 정보를 기록하기 위한 리스트
visited = [False] * 8

def bfs(n):
    visited[n] = True
    qu = deque()
    qu.append(n)
    while qu :   # len(qu) > 0
        tmp = qu.popleft()
        print(tmp)
        for nx in graph[tmp] :
            if visited[nx] == False :
                qu.append(nx)
                visited[nx] = True

bfs(1)


# extra - 주사위 던지기

path = []

def throw(n):
    if n == 3 :
        print(path)
        return
    for i in range(1, 7):
        path.append(i)
        throw(n+1)
        path.pop()

throw(0)
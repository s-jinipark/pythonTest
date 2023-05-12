
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
print(visited)

def dfs(n):
    print(n)
    visited[n] = True
    for nx in graph[n] : # 다음거
        if visited[nx] == False : # 방문 안했다
            dfs(nx)

# 탐색 시작 노드 1을 넣어주며 dfs() 실행
dfs(1)  # -> 1부터 시작이라는


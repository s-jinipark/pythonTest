
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

# 재차 연습 -->
visited = [False] *9

def dfs(v) :
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if visited[i] is False :
            dfs(i)
dfs(1)

# //<--

# 방문
# visited = [False] * 9  # 하나 커야 됨
#
# def dfs(v) :
#     # 방문 표시
#     visited[v] = True
#     print(v)
#     # 인접 노드 방문
#     for i in graph[v]:
#         #print(i, end=' ')
#         # 방문하지 않았다면
#         if not visited[i] :
#             dfs(i)
#     #print()
#
# dfs(1)


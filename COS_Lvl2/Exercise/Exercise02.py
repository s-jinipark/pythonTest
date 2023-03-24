
vertex = [[1, 2],[1, 7], [2, 8], [7, 8], [7, 3], [7, 5], [8, 6], [5, 6], [5, 3], [3, 4],[4, 6]]
# 그래프로 만듬

graph = [[] for _ in range(9)]
print(graph)

for v in vertex :
    #print(v)
    graph[v[0]].append(v[1])
    graph[v[1]].append(v[0])

print(graph)

# 이 이후는 동일하다
visited = [0] * 9

def dfs(n):
    print(n)
    visited[n] = 1
    for i in graph[n] :
        #print('>', i)
        if visited[i] == 0 :  # 방문 안 했다면
            dfs(i)

dfs(1)



# 정점의 수 N , 간선의 수 M , 시작 정점 R

n, m, r = map(int, input().split())
#-> 5 5 1 입력

graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
count = 1

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


#graph = [[], [4, 2], [1, 3, 4], [2, 4], [1, 2, 3], []]
print(graph)

def bfs(n):
    global  count
    visited[n] = count
    q  = []
    q.append(n)
    while len(q) > 0 :
        tmp = q.pop(0)
        graph[n].sort()
        for i in graph[tmp] :
            print(i)
            if visited[i] == 0 :
                count += 1
                q.append(i)
                visited[i]=count

bfs(1)
print('-----')
#print(visited)
for i in range(1, len(visited)):
    print(visited[i])

'''

dfs(V, E, R) {  # V : 정점 집합, E : 간선 집합, R : 시작 정점
    visited[R] <- YES;  # 시작 정점 R을 방문 했다고 표시한다.
    for each x ∈ E(R)  # E(R) : 정점 R의 인접 정점 집합.(정점 번호를 내림차순으로 방문한다)
        if (visited[x] = NO) then dfs(V, E, x);
}
'''
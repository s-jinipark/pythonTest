
#from collections import deque
import sys
input = sys.stdin.readline

# 첫째 줄에는 컴퓨터의 수
# 둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수

# com_cnt = int(input())
# match_cnt = int(input())

com_cnt = 7
match_cnt = 6


graph = [[] for _ in range(com_cnt + 1)]
visited = [0] * (com_cnt+1)


# for _ in range(match_cnt):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

print(graph)
graph = [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]


def dfs(n):
    visited[n] = 1
    for i in graph[n]:
        if visited[i] == 0 :
            dfs(i)

dfs(1)
print(visited)

cnt = 0
for i in range(2, len(visited)) :
    if visited[i] == 1 :
        cnt += 1
print(cnt)
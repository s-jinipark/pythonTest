
import sys
from collections import deque

sys.stdin = open("input_046.txt", "rt")

# 도시의 개수(N), 도로의 개수(M), 거리 정보(K), 출발 도시의 번호(X)

N, M, K, X = map(int, input().split())
print(N, M, K, X)

'''
최단 거리가 K 인 모든 도시들의 번호 출력

'''
A = [[] for _ in range(N+1)]
answer = []
visited = [-1] * (N+1)  # -1 로 셋팅

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] += 1   # 이 부분 먼저 처리
    while queue :
        now_node = queue.popleft()
        for i in A[now_node]:
            print(i)
            if visited[i] == -1 :
                queue.append(i)
                visited[i] = visited[now_node] +1

#print(A)
for _ in range(M):
    s, e = map(int, input().split())
    A[s].append(e)
print(A)

BFS(X)
print(visited)

for i in range(N+1):
    if visited[i] == K :
        answer.append(i)

if not answer:
    print(-1)
else :
    answer.sort()
    for i in answer:
        print(i)



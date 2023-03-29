
import sys

sys.stdin = open("input_c05-023.txt", "rt")

def DFS(v):
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)

n, m = map(int, input().split())  # 노드 개수, 에지 개수
A = [[] for _ in range(n+1)]
visited = [False] * (n+1)

print(n, m, A, visited)

for _ in range(m):
    s, e = map(int, input().split())
    A[s].append(e)  # 양방향 에지이므로 양쪽에 에지를 더하기
    A[e].append(s)
print(A)

count = 0

for i in range(1, n+1):
    if not visited[i]:  # 연결 노드 중 방문하지 않았던 노드만 탐색
        count += 1
        DFS(i)

print(count)

'''
모든 노드를 탐색하여 탐색 종료 -> DFS 총 2회 수행
즉, 연결 요소 개수 = 2

만약 그래프가 모두 연결되어 있었다면 DFS 는 1번 실행되었을 것
다시말해 모든 노드를 탐색하는데 실행한 DFS 의 실행 횟수가 곧 연결 요소의 개수와 같음

[my]

'''

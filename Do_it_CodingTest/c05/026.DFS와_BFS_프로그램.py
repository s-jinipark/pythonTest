
import sys

sys.stdin = open("input_c05-026.txt", "rt")


n, m, start = map(int, input().split())  # 노드 개수, 에지 개수, 시작점
A = [[] for _ in range(n+1)]
visited = [False] * (n+1)  # [-> n+1 임]

print(n, m, start, A, visited)

for _ in range(m):
    s, e = map(int, input().split())
    print(s, e)
    A[s].append(e)
    A[e].append(s)

#print(A)

'''
문제 조건에서 작은 번호의 노드부터 탐색한다 함
인접 노드를 오름차순으로 정렬

[my]

'''

for i in range(n+1) :
    A[i].sort()  # 번호가 작은 노드부터 방문하기 위해 정렬하기
print(A)


def DFS(v) :
    print(v, end=' ')
    visited[v] = True
    for i in A[v]:  # [ v 에 붙어 있는 리스트 탐색 ]
        if not visited[i]:
            DFS(i)

visited = [False] * (n+1)
DFS(start)

print('\n--------------------')
from collections import  deque

def BFS(v) :
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue :
        now_node = queue.popleft()
        print(now_node, end=' ')
        for i in A[now_node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

visited = [False] * (n+1)
BFS(start)


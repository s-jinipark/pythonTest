
import sys
from collections import deque

sys.stdin = open("input_047.txt", "rt")

# 컴퓨터 개수 (노드) , 신뢰 관계 (에지)

N, M  = map(int, input().split())
print(N, M)

'''
2번째 줄부터 M 개의 줄에 신뢰하는 관계가 'A B' 와 같은 형식으로 들어 옴
'A 가 B 를 신뢰한다' 를 의미

'''

A = [[] for _ in range(N+1)]
print(A)
#visited = [-1 for _ in range(N+1)]
#print(visited)
answer = [0] * (N+1)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue :
        now_node = queue.popleft()
        for i in A[now_node]:
            print(v, '-', i)
            if not visited[i]:
                visited[i] = True
                answer[i] += 1
                queue.append(i)

for i in range(M) :
    s, e = map(int, input().split())
    #print(s, e)
    A[s].append(e)
print(A)

# 모든 노드에서 BFS 실행 ??? [이게 다른 점 ?? ...]
for i in range(1, N+1) :
    visited = [False] * (N+1)
    BFS(i)

print(answer)
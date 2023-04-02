
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
print(A)
for _ in range(M):
    s, e = map(int, input().split())
    A[s].append(e)
print(A)


visted = [-1] * (N+1)
print(visted)
queue = deque()
queue.append(X)
visted[X] += 1   # [여기] 이거 없어서 값이 하나 적게 나옴

while queue :
    now_node = queue.popleft()
    for i in A[now_node] :
        print(i)
        if visted[i] == -1 :
            visted[i] = visted[now_node] +1
            queue.append(i)

print(visted)

######################### 책 조금씩 참고하면서 했는데, 위 [여기] 참조
print('#########################')



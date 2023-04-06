
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

#A2 = [[] for _ in range(N+1)]  # N+1 의 이유는 index 와 노드의 번호를 맞추기 위해...
#print(A2)
print(A)   #  이미 읽은 값 활용
visted = [-1 for _ in range(N+1)]
print(visted)

queue = deque()

def BFS(v):
    queue.append(v)  # 일단 넣고
    visted[v] += 1  # 방문도 chk
    while queue :
        now_node = queue.popleft()  # 이제 꺼내야지...
        for i in A[now_node]:
            print(i)
            if visted[i] == -1:
                queue.append(i)
                visted[i] = visted[now_node] + 1

BFS(X)
print(visted)

for i in range(N+1):  # 여기도 +1 까지
    #print(visted[i])
    if visted[i] == K:
        print(i)

''' 조건에 맞지 않을 경우 -1 을 출력해야 하므로
    answer 라는 list 에 넣고
    list 에 값이 없을 경우 -1 출력 하는 과정 거침
'''
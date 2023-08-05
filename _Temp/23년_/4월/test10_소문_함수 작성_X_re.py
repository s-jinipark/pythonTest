
# 소문
from collections import deque

def solution(n, k, acquaintance):
    answer = 0
    for a in acquaintance:
        adj[a[0]].append(a[1])
        adj[a[1]].append(a[0])
    print(adj)
    # 인프런 에선 어떻게 했지? 기억 안남
    # 일단 이렇게 연결을 [[], [2], [1, 3], [2], [5], [4], [] ...

    q = []    # 그냥 리스트에다가
    q.append(1)  # 1번 시작 ~
    visited[1] = 1  # 방문 chk
    dist[1] = 0  # 시작점이니까 0
    while len(q):
        cur = q[0]  # 맨 앞 뺀다
        q.pop(0)
        for next in adj[cur]:
            if visited[next] == 0:
                visited[next] = 1
                dist[next] = dist[cur] + 1
                q.append(next)
                print('append next', next)
    return dist[k]
    #return answer

'''

'''

adj = [[] for _ in range(101)]
visited = [0 for _ in range(101)]
dist = [-1 for _ in range(101)]   # 거리를 나타내며, -1 로 셋팅

n = 5  #재학생 수를 나타내는 정수 n과 학생 번호 k,
k = 3
#acquaintance = [[1, 2], [3, 2], [4, 5]]
acquaintance = [[2, 3], [4, 3], [3, 5]]

an = solution(n, k, acquaintance)
print('an = ', an)


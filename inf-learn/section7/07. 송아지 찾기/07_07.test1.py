
# BFS 는 최단 거리 구할 때
from collections import deque

def solution():
    answer = 0
    qu = deque()
    #start 는 5
    qu.append(S)
    visted[S] = 1
    distan[S] = 0 # 여긴 0 ?
    while qu:
        now = qu.popleft()
        if now == E :
            break
        for next in (now+1, now-1, now+5): # 이렇게 하면 3가닥으로, ([주] range 가 없음)
            print('>', next)
            if 0 <= next <= Max :  # = 도 포함
                if visted[next] == 0:
                    qu.append(next)
                    visted[next] =1
                    distan[next] = distan[now] +1
        print(now, distan[E])

    return answer


S = 5   # 위치 start
E = 14  # 위치 end
Max = 10000
visted = [0] * (Max+1)
distan = [0] * (Max+1)

re = solution()
print('re :', re)
#=>
print('==============================')

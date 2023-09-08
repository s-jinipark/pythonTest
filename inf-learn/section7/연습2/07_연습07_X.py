
##### 송아지 찾기(BFS : 상태트리탐색)

from collections import  deque
def solution():
    answer = 0

    '''
    이전에도 못 품
    
    어캐 풀었는데, 답도 틀림
    '''
    qu = deque()

    # 5 를 넣고 시작
    qu.append(s)
    chk[s] = 1
    dis[s] = 0

    while qu:  # 비어 있으면 멈춤
        now = qu.popleft()
        if now == e:
            break
        for next  in (now-1, now+1, now+5):   # 3가지...
            if 0 < next <= MAX :
                if chk[next] == 0 :
                    qu.append(next)
                    chk[next] = 1
                    dis[next] = dis[now]+ 1
    print(dis[e])

#inp = '25114'
s = 5
e = 14

# [2]
MAX = 10000
dis = [0] * (MAX+1)   #(e+1)  # 0 번 부터
chk = [0] * (MAX+1)   #(e+1)  # 방문 체크
jump = [-1, 1, 5]  # 한 번의 점프로 앞으로 1, 뒤로 1, 앞으로 5를 이동할 수 있다.

re = solution()
print(re)
#=>
print('====================')

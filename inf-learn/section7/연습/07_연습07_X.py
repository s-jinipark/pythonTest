
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

    while qu:
        cur = qu.popleft()
        if cur == e:
            print(dis[cur])
            break
        for j  in jump:
            if 0 < j <= 100 and chk[cur+j] == 0 :
                chk[cur+j] = 1
                qu.append(cur + j)
                if dis[cur+j]  == 0 :
                    dis[cur+j] += dis[cur] +1

#inp = '25114'
s = 5
e = 14

dis = [0] * 100  #(e+1)  # 거리, 순번을 저장
chk = [0] * 100  #(e+1)  # 방문 체크
jump = [-1, 1, 5]  # 한 번의 점프로 앞으로 1, 뒤로 1, 앞으로 5를 이동할 수 있다.

re = solution()
print(re)
#=>
print('====================')

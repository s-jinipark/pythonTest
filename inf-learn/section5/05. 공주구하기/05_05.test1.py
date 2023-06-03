from collections import deque

# 프로그래머스 스타일 로 ...
def solution(N, K):
    answer = 0

    qu = deque()

    for i in range(1, N+1):
        qu.append(i)
    print(qu)  # deque([1, 2, 3, 4, 5, 6, 7, 8])

    cnt = 1
    while len(qu) > 1 :
        if cnt % K == 0 :
            qu.popleft()
        else:
            qu.append(qu.popleft() )
        cnt += 1

    print(qu[0])
    answer = qu[0]

    ########## first
    # qu = []
    #
    # for i in range(1, N+1):
    #     qu.append(i)
    # print(qu)
    #
    # cnt = K
    # while len(qu) > 1 :
    #     del(qu[cnt-1])
    #     print(qu)

    return answer

N = 8
K = 3

re = solution(N, K)
print('re :', re)
#=> 12
print('==============================')



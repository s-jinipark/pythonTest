
##### 응급실

from collections import  deque


def solution():
    answer = 0
    '''
    풀이 보고 ...
    이거 암기 하던지 해야 겠다
    '''
    qu = deque()
    # 적재
    for i in range(N):
        qu.append((i, inp[i]))

    print(qu)
    cnt = 0
    while True:
        cur = qu.popleft()
        if any(cur[1] < x[1]  for x in qu):
            # 웁스 이런거 몰랐다..  하나라도 있으면, 참
            qu.append(cur)
        else :
            cnt += 1
            if cur[0] == M :
                print(cnt)
                break

    return answer

N = 5
M = 2
inp = [60, 50, 70, 80, 90]

re = solution()
print(re)
#=> 3
print('====================')

N = 15
M = 5
inp = [63,53,87,91,83,72,83,92,63,68,88,74,51,82,89 ]

re = solution()
print(re)
#=> 10

##### 응급실

from collections import  deque
def chk_high(x, q):
    for i in q:
        #print('>', i)
        if x < i[1]:
            return False
    return True

def solution():
    answer = 0
    '''
    몇번째 였는지를 알아야 하니까 
    2차원 배열 or 튜플에 넣어야.
    '''
    qu = deque()
    # 적재
    for i in range(N):
        qu.append((i, inp[i]))

    print(qu)

    # 진료
    while qu:
        #idx, prir =  qu.popleft()
        #print(idx, prir , qu)
        #=> 다시 넣어야 되서 튜플단위로
        tmp = qu.popleft()
        # 현재 값보다 높은게 있는지 확인하는 함수
        print(tmp )
        print ( chk_high( tmp[1] , qu ) )
        if chk_high( tmp[1]  , qu ) and len(qu) > 0:
            qu.append(tmp )
        else:
            answer +=1
            if tmp[0] == M :
                break
    print(qu)
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
#=> 답 10, 난 6
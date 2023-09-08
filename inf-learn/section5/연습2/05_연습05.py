
##### 공주 구하기(큐 자료구조로 해결)

from collections import  deque

def solution():
    answer = 0

    '''
    1부터 시작하여 번호를 외치게 한다. 
    한 왕자가 K(특정숫자)를 외치면 그 왕자는 공주를 구하러 가는데서 제외되고 원 밖으로 나오게 된다. 
    그리고 다음 왕자부터 다시 1부터 시작하여 번호를 외친다.
    [그 다음 왕자가 1이라는]
    '''
    qu = deque()
    # 적재
    for i in range(1, N+1):
        qu.append(i)

    while len(qu) > 1 :
        # K 를 외친 ..
        for j in range(K):
            tmp = qu.popleft()
            if j < K-1 :
                qu.append(tmp)
        print(qu)
    answer = qu.pop()
    return answer

N = 8
K = 3   # K를 외친 왕자 제외

re = solution()
print(re)
#=> 7
print('====================')

N = 500
K = 8   # K를 외친 왕자 제외

re = solution()
print(re)
#=> 494
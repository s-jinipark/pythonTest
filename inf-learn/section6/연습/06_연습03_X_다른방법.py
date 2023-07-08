
##### 부분집합 구하기(DFS)

from itertools import  combinations

def solution():
    answer = 0

    # 데이터 적재
    tmp = []
    for i in range(1,N+1):
        tmp.append(i)
    print(tmp)

    # combination 으로
    result = []
    for j in range(N+1):
        #print(combinations(tmp, j))   # 흠 이렇게 하면, <itertools.combinations object at 0x00000205D7D273D0>
        print( list( combinations(tmp, j)) )

    return answer

N = 3
#ch = [0] * (N+1)

re = solution()
print(re)
#=>
print('====================')


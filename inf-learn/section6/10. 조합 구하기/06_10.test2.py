
from itertools import combinations

def solution(N, M):
    answer = 0

    tmp = []
    for i in range(1, N+1):
        tmp.append(i)
    print(tmp)

    tmp2 = list(combinations(tmp, M))
    print(tmp2)

    return answer

N = 4   # 1부터 N까지 번호가 적힌 구슬
M = 2   # 이 중 M개를 뽑는 방법의 수

re = solution(N, M)

print('re :', re)
#=>
print('==============================')

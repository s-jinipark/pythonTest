
from itertools import combinations

def solution():
    answer = 0

    print(inp)

    tmp = list(combinations(inp, K))
    print(tmp)

    for t in tmp :
        print(t)
        t_sum = sum(t)
        print(t_sum)
        if t_sum % M == 0 :
            answer += 1

    return answer

N = 4   # 정수의 개수
K = 2   # 임의의 정수 (K 개를 뽑는 ...)
inp = [2,4,5,8,12]
M = 6

re = solution()

print('re :', re)
#=>
print('==============================')

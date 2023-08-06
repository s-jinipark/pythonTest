
# 소문
from collections import deque

def solution(n, k, acquaintance):
    answer = 0
    for a in acquaintance:
        a= a.sort()
    print(acquaintance)

    start = 1
    qu = deque()
    qu.append(start)


    return answer

'''

'''

n = 5  #재학생 수를 나타내는 정수 n과 학생 번호 k,
k = 3
acquaintance = [[1, 2], [3, 2], [4, 5]]

an = solution(n, k, acquaintance)
print('an = ', an)


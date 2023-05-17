from itertools import permutations

def solution(n, k):
    answer = []

    tmp = []
    for i in range(1, n+1):
        tmp.append(i)
    print(tmp)

    lst = (list) (permutations(tmp , 3))
    print(lst)
    answer = (list)(lst[k-1])
    return answer

n = 3
k = 5

re = solution(n, k)
print(re)

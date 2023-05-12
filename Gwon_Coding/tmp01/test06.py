from itertools import combinations

# N, M = map(int, input().split())

N = 4
M = 2
lst = []
test1 = []

def dfs(start):
    if len(lst) == M :
        print(' '.join(map(str, lst)))
        return
    for i in range(start, N+1):
        if i not in lst:
            lst.append(i)
            dfs(i+1)
            lst.pop()

dfs(1)

# https://jiwon-coding.tistory.com/22
# 외울 거
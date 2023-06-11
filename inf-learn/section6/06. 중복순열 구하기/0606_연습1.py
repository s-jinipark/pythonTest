
# self
# 생각 안나서 풀이 봄
def DFS(v):
    #global  rtn

    if v == M :
        print(res)
        return
    else :
        for i in range(1, N+1):  # 여기서 N 개로 뻗어야 됨
            res[v] = i
            DFS(v+1)

def solution(N):
    answer = 0
    lst = []

    DFS(0)

    return answer

# 1부터 N까지 번호가 적힌 구슬이 있습니다.
# 이 중 중복을 허락하여 M번을 뽑아 일렬로 나열하는 방법을 모두 출력합니다.
N = 3
M = 2
#rtn = ''
res = [0] * M  # M 만큼 뽑으니까 M 만 있으면 됨

re = solution(N)
print('re :', re)

#print(rtn)

'''
res 를 M 만큼 만들고..
N 번 만큼 뻗는다는...
'''

# 만약 생각 안 났을 때.. (구현에서)
from itertools import product

lst = [1,2,3]
rtn = list(product(lst, lst))
#rtn = list(product(lst, lst, lst))
print(rtn)




# self
def DFS(L):
    global  res

    if L == M :  # 종료조건
        # 같은 수 나온 경우 제거
        if res[M-1] != res[M-2]:
            print(res)
            return
    else :
        for i in range(1, N+1):  # 1 부터 ~ N 까지  (**)
            res[L] = i
            DFS(L+1)

def solution(N):
    answer = 0

    DFS(0)

    return answer
# 1부터 N까지 번호가 적힌 구슬이 있습니다.
# 이 중 M개를 뽑아 일렬로 나열하는 방법을 모두 출력합니다.
N = 3
M = 2
#rtn = ''
res = [0] * M

re = solution(N)
print('re :', re)


# 함수로 테스트
from itertools import permutations

inp = [1,2,3]
rtn = list(permutations(inp, 2))
print(rtn)

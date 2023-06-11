
# self
# 풀이 봄 (중요하다고 강조)
def DFS(L, s):
    global  res

    if L == M :  # 종료조건
        print(res)
        return
    else :
        for i in range(s, N+1):  # s 부터 뻗는다 (**)
            res[L] = i
            #DFS(L+1, s+1)
            DFS(L + 1, i + 1)  # i+1 임 , 강사도 헷갈림

def solution(N):
    answer = 0

    DFS(0, 1)   # 인자가 하나 더 있음 s (start)

    return answer
# 1부터 N까지 번호가 적힌 구슬이 있습니다.
# 이 중 M개를 뽑는 방법의 수를 출력
N = 4
M = 2
#rtn = ''
res = [0] * M

re = solution(N)
print('re :', re)

# 이거 함수로
from itertools import  combinations
inp = [1,2,3,4]
rtn = list(combinations(inp, M))
print(rtn)


# self
def DFS(L, sum):
    global  res
    # [2] 이건 컷팅
    if L > res :
        return

    if sum > M :  # 종료조건은 15 보다 커지면
        return

    if sum == M :
        if L < res :
            res = L
    else :
        for i in range(N):  # 여기서 N 개로 뻗어야 됨 (**)
            DFS(L+1, sum+inp[i])

def solution(N):
    answer = 0

    DFS(0, 0)

    return answer

N = 3   # 동전의 종류
inp = [1,2,5]
M = 15  # 거스름
#rtn = ''
inp.sort(reverse=True)  # 큰 동전 부터..
res = 2147000000

re = solution(N)
print('re :', re)

print(res)

'''
3가닥으로 뻗는 거.
레벨 L 이 동전의 갯수 (이게 중요.)

'''


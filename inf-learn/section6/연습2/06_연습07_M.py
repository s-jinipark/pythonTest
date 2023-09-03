
##### 동전교환
def DFS(L, sum):
    global  min_val
    if sum > 15 :
        return
    if sum == 15 :
        print(res, L)  # [2] 헐 L (레벨) 수를 세니 동전의 갯수가 된다
        tmp = 0
        for i in range(N):
            tmp += res[i]
        if tmp < min_val:
            min_val = tmp
        return
    else :
        # 3가닥으로 뻗어야... [가닥 뻗는 것만 잘 생각해도...]
        for i in range(N):
            res[i] += 1
            DFS(L+1, sum + inp[i])
            res[i] -= 1  # 빼줘야 하나?

def solution():
    answer = 0

    # [2] 큰 거 부터 하도록 ...
    #inp.sort(reverse=True)  # 이 건 꼭 필요한가? 다 돌건데..

    DFS(0,0)
    print('min_val:', min_val)
    return answer

N = 3  # 동전의 갯수
inp = [1,2,5]
M = 15  # 거슬러 줄 금액
res = [0] * N  # 동전 종료 만큼
sum = 0
min_val = 2147000000

re = solution()
print(re)
#=>
print('====================')


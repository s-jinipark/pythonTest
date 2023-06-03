
def DFS(L, sum) :
    global res
    if sum > M:  # M 보다 크면 cutting
        return
    if L > res :
        return
    if sum == M :  # 중지 조건이 Level 이 아니라 sum 임
        # print(L, res)
        # return
        if L < res :
            res = L
    else :
        for c in coin:
            #res += 1   # [2] X
            #print('>', sum+c)
            DFS(L+1, sum+c)

def solution(coin, M):
    answer = 0
    coin.sort(reverse=True)  # 가장 큰 동전부터

    DFS(0, 0)  # Level, Sum 으로..
    print(res)
    return answer

N = 3   # 동전의 종류
coin = [1,2,5]   # 동전 종류
M = 15  # 거슬러 줄 금액
res = 2147000000
re = solution(coin, M)

print('re :', re)
#=>
print('==============================')


N = 5   # 동전의 종류
coin = [1,5,7,11,15]   # 동전 종류
M = 39  # 거슬러 줄 금액
res = 2147000000
re = solution(coin, M)

print('re :', re)
#=> 5
print('==============================')


N = 5   # 동전의 종류
coin = [1,8,20,25,50]   # 동전 종류
M = 129  # 거슬러 줄 금액
res = 2147000000
re = solution(coin, M)

print('re :', re)
# #=>
print('==============================')

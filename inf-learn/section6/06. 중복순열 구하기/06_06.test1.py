
def DFS(L, res):
    global cnt
    if L == M :
        print(res)
        cnt += 1
    else :
        for i in range(1, N+1):  # 3가닥으로 뻗어야 한다는 ...
            res[L] = i
            DFS(L+1, res)

def solution(N, M):
    answer = 0
    res = [0] * M  # M 개 뽑는 거
    #print(res)
    DFS(0, res)
    print(cnt)
    return answer

N = 3   # 1부터 N까지 번호가 적힌 구슬
M = 2   # 중복을 허락하여 M번 뽑는다
cnt = 0

re = solution(N, M)

print('re :', re)
#=>
print('==============================')

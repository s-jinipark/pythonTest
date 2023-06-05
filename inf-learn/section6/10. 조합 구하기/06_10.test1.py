
def chk_dup(res):
    dict = {}
    for r in res:
        if r  in dict:
            return False
        else :
            dict[r] = 1
    return True

def DFS(L, res):
    if L == M :
        if not chk_dup(res):
            return
        print(res)
        return
    else :
        for i in range(1, N+1):
            res[L] = i
            DFS(L+1, res)

def solution(N, M):
    answer = 0

    res = [0] * M
    DFS(0, res)
    return answer

N = 4   # 1부터 N까지 번호가 적힌 구슬
M = 2   # 이 중 M개를 뽑는 방법의 수

re = solution(N, M)

print('re :', re)
#=>
print('==============================')

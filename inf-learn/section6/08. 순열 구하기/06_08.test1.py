
def DFS(L, res):
    if L == M :
        if res[0] == res[1]:   # cutting  # 이건 2개 뽑을 때만 되는..
            return
        print(res)
        return
    else:
        for i in range(1, N+1) :  # 1부터 라고 해서
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
M = 2   # M 개를 뽑아 일렬로 나열
cnt = 0

re = solution(N, M)

print('re :', re)
#=>
print('==============================')

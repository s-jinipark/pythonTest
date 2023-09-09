
##### 순열 구하기
def DFS(L):
    if L == M :
        print(res)
        return
    else:
        for i in range(1, N+1):
            if ch[i]==0:
                res[L] = i
                ch[i] = 1
                DFS(L+1)
                ch[i] = 0

    # if L == M :
    #     print(res)
    #     return
    # else:
    #     for i in range(1, N+1):
    #         if i in res :
    #             continue
    #         res[L] = i
    #         DFS(L+1)
    #         res[L] = 0   # [2] 웁스~ 이거 없으니까 안 됨

def solution():
    answer = 0
    '''
    6번의 중복순열 에서 중복안되게 ..
    [1] visited 를 하면 될거 같음 ..
    [2] 검색해서 하는 방식으로 먼저 ..
    '''
    DFS(0)

    return answer

N = 3  # 구슬의 갯수

M = 2  # 뽑는 갯수
res = [0] * M
sum = 0
min_val = 2147000000
ch = [0] * (N+1) # N+1 로 하고 1부터 사용

re = solution()
print(re)
#=>
print('====================')


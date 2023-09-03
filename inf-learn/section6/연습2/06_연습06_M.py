
##### 중복순열 구하기
def DFS(L):
    global cnt
    if L == M:
        print(res)
        cnt += 1
        return
    else:
        for i in range(1, N+1):
            res[L]=i
            DFS(L+1)
            res[L] = 0  # 굳이? => 안해도 될 듯

def solution():
    answer = 0

    DFS(0)
    '''
    여기서 3개로 뻗어야 되지 않나?
    뽑은 번호 저장이 여기에는 필요하다는 사실
    '''
    return answer

N = 3  # 구슬 1부터 3
M = 2  # M번 뽑는다
res = [0] * M  # 뽑은 구슬 번호 저장
cnt = 0

re = solution()
print(re)
print(cnt)
#=>
print('====================')


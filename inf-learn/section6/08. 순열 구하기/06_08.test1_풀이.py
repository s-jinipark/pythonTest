
def DFS(L):
    if L == M :
        print(res)
        return
    else:
        for i in range(1, N+1):
            #print('>', i)
            if chk[i] == 0:  # 방문 안한 경우만 (*)
                chk[i] = 1
                res[L] = i
                DFS(L+1)
                chk[i] = 0  # 마지막 원 위치(**)

def solution(N, M):
    answer = 0

    #print(res)
    DFS(0)
    print(cnt)
    return answer

N = 3   # 1부터 N까지 번호가 적힌 구슬
M = 2   # M 개를 뽑아 일렬로 나열
cnt = 0
# 전역으로
res = [0] * M  # M 개 뽑는 거
chk = [0] * (N+1)

re = solution(N, M)

print('re :', re)
#=>
print('==============================')

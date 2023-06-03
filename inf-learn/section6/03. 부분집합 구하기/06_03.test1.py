
def DFS(x, chk):
    if x == n+1 :
        #print(x, chk, n)
        for i in range(1, n+1):
            if chk[i]==1:
                print(i, end=' ')
        print()
    else:
        chk[x] = 1
        DFS(x+1, chk)
        chk[x] = 0
        DFS(x+1, chk)

def solution(N):
    answer = 0
    global n
    n = N
    #global chk
    # 사용 여부를 chk
    # 2 가지 경우 수 가 있음(사용 한다, 사용하지 않는다)
    # -> 상태 트리
    chk = [0] * (n+1)  # 한개 더
    DFS(1, chk)

    return answer

N = 3

re = solution(N)
print('re :', re)
#=>
print('==============================')

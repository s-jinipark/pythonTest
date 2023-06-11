

def DFS(N):
    global rtn
    print(N//2, N%2)
    nam = N % 2
    rtn = str(nam) + rtn
    N = N // 2

    if N == 0 :  # 종료 조건.
        return
    else :
        DFS(N)


def solution(N):
    answer = 0

    DFS(N)

    return answer

N = 11
rtn = ''

re = solution(N)
print('re :', re)

print(rtn)

'''
종료 조건을 처음에는 N < 1 이렇게 했다가
N == 0 으로 ...
'''
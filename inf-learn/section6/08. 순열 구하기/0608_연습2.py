
# 풀이 본 후
def DFS(L):
    global  res

    if L == M :  # 종료조건

        print(res)
        return
    else :
        for i in range(1, N+1):  # 1 부터 ~ N 까지  (**)
            if ch[i] == 0 :  # 방문 안 했다는 얘기지.
                ch[i] = 1
                res[L] = i
                DFS(L+1)
                ch[i] = 0  # 이거 없으면 안됨

def solution(N):
    answer = 0

    DFS(0)

    return answer
# 1부터 N까지 번호가 적힌 구슬이 있습니다.
# 이 중 M개를 뽑아 일렬로 나열하는 방법을 모두 출력합니다.
N = 3
M = 2
#rtn = ''
res = [0] * M
ch = [0] * (N+1)

re = solution(N)
print('re :', re)




# self
def DFS(v, sum):
    global  rtn
    if v == N: # 종료 조건
        print(sum)
        if sum <= C and sum > rtn : # 제한 C 를 넘지 않으면서, 가장 큰 값
            rtn = sum
        return
    else :
        DFS(v+1, sum + inp[v])
        DFS(v+1, sum )

def solution(N):
    answer = 0

    DFS(0, 0)  # 인자 두개고, sum 을 넘김

    return answer

# C를 넘지 않으면서 그의 바둑이들을 가장 무겁게 태우고 싶다.
C = 259
N = 5
inp = [81,58,42,33,61]
#rtn = ''
rtn = 0

re = solution(N)
print('re :', re)

print(rtn)


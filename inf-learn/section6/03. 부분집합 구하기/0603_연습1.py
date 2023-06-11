
# self
def DFS(v, ghap):

    if v == N :
        if len(ghap) == 0:  # 공집합 제거
            return
        print(ghap)
        return
    else :
        DFS(v+1, ghap)
        ghap.append(v+1)
        # 선택하는가 or 안 하는가?
        DFS(v+1, ghap)
        ghap.pop()


def solution(N):
    answer = 0
    ghap = []
    DFS(0, ghap)   # 0부터 ?

    return answer

# 자연수 N이 주어지면 1부터 N까지의 원소를 갖는 집합의 부분집합을 모두 출력하는 프로그램
N = 3
#rtn = ''

re = solution(N)
print('re :', re)

#print(rtn)


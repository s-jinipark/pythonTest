
# 풀이 본 후
def DFS(v):

    if v == N+1 :  # 여기도 맞춰서 +1
        #print(ch)
        for i in range(1, N+1):
            if ch[i] ==  1 :
                print(i, end=' ')
        print()

        return
    else :
        ch[v] =1  # 사용한다 안한다의 구분
        DFS(v+1)
        ch[v] =0
        DFS(v+1)


def solution(N):
    answer = 0

    DFS(1)   # 1부터 ?

    return answer

# 자연수 N이 주어지면 1부터 N까지의 원소를 갖는 집합의 부분집합을 모두 출력하는 프로그램
N = 3
#rtn = ''
ch = [0] * ( N +1 )  # 앞에 하나 여유를 두겠다는

re = solution(N)
print('re :', re)

#print(rtn)


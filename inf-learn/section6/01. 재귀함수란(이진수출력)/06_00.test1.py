
def DFS(x):
    if x > 0 :
        #print(x)  # 3 2 1 이 출력
        DFS(x-1)
        print(x)  # 여기에 두면 1 2 3 이 출력


def solution(N):
    answer = 0
    DFS(N)

    return answer

N = 3

re = solution(N)
print('re :', re)
#=>
print('==============================')


def DFS(x):
    # 7까지 출력
    if x > 7 :
        return
    else:
        #print(x, end=' ')
        DFS(x * 2)
        DFS(x * 2 + 1)
        print(x, end=' ')

def solution(N):
    answer = 0

    DFS(N)

    return answer

N = 1

re = solution(N)
print('re :', re)
#=>
print('==============================')

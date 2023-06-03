import sys

def DFS(L, sum):
    if L == N :
        if sum==(total-sum):
            print('YES')
            sys.exit(0)  # 프로그램 나가기 ? , 코딩테스트에서는 이래도 되는지 ?
    else :
        DFS(L+1, sum+inp[L])
        DFS(L+1, sum)

def solution(N, inp):
    answer = '' #0
    #chk = [0] * N
    DFS(0,  0)  # level 과 sum 을 표시

    return answer

N = 6
inp = [1,3,5,6,7,10]
total = sum(inp)
re = solution(N, inp)
print('re :', re)
#=>
print('==============================')

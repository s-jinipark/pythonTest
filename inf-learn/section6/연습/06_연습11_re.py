
##### 수들의 조합

def DFS(L, S, sum):  # sum 을 따로 하지 않고
    global  cnt

    if L == K :  # 종료 조건
        if sum % M == 0:
            cnt +=1
    else:

        for i in range(S,N):
            DFS(L+1, i+1, sum+inp[i])
            # if ch[i] == 0 :  # 이게 필요 없네...
            #     res[L] = inp[i]
            #     ch[i] =1
            #     DFS(L+1, i+1)
            #     ch[i] =0

def solution():
    answer = 0

    #DFS(0, 0)
    # 풀이 보고
    DFS(0, 0, 0)
    print(cnt)
    return answer

N = 5  # 정수의 개수
K = 3  # K 개 뽑는 조합
inp = [2,4,5,8,12]
M = 6  # 임의의 정수

res = [0] * K
ch = [0] * (N+1)
lst = []

cnt = 0

re = solution()
print(re)
#=>
print('====================')

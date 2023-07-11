
##### 수들의 조합

def DFS(L, S):
    global  cnt

    if L == K :  # 종료 조건
        print(res, sum(res))
        if sum(res) % M == 0:
            cnt +=1
    else:
        # [3]
        for i in range(S,N):
            if ch[i] == 0 :
                res[L] = inp[i]
                ch[i] =1
                DFS(L+1, i+1)
                ch[i] =0

        # [2]
        #조합이니 [1, 2, 3] 과 [3, 2, 1]  중복 => 하나로
        # for i in range(N):
        #     if ch[i] == 0 :
        #         res[L] = inp[i]
        #         ch[i] =1
        #         DFS(L+1, S)
        #         ch[i] =0

        # [1] 중복 다 나오는
        # for i in range(N):
        #     res[L] = inp[i]
        #     DFS(L+1, S)

def solution():
    answer = 0

    DFS(0, 0)
    #DFS(0, 1)
    print(cnt)
    return answer

N = 5  # 정수의 개수
K = 3  # K 개 뽑는 조합
inp = [2,4,5,8,12]
M = 6  # 임의의 정수
# M 의 배수의 개수 ??

res = [0] * K
ch = [0] * (N+1)
lst = []

cnt = 0

re = solution()
print(re)
#=> 2
print('====================')

N = 12  # 정수의 개수
K = 5  # K 개 뽑는 조합
inp = [2,4,5,8,12,7,13,1,3,16,19,22]
M = 7  # 임의의 정수

res = [0] * K
ch = [0] * (N+1)
lst = []

cnt = 0

re = solution()
print(re)
#=> 114



##### 수들의 조합
def DFS(L , s):
    global  cnt
    if L == K :
        #print(res)
        tmp = 0
        for r in res:
            tmp += inp[r]
        #print(tmp)
        if tmp % M == 0:
            print(tmp)
            cnt += 1
        return
    else :
        for i in range(s, N):
            res[L] = i
            DFS(L+1, i+1)

def solution():
    answer = 0

    DFS(0, 0)  # 이경우는 0 번 idx 에서 시작해야 해서
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



##### K 번째 약수
def solution(N, K):
    answer = 0
    tmp = []
    for i in range(1, N+1):
        #print(i)
        if N%i == 0 :
            tmp.append(i)
    # 몇 번째는 1 부터 시작하고
    # tmp 는 0 부터 시작
    if len(tmp) < K :
        answer = -1
    else:
        # 순서대로 들어가 있으므로
        answer = tmp[K-1]  # 여기서는 -1 해주어야
    return answer

N = 6
K = 3
re = solution(N, K)
print(re)
#=> 3

N = 25
K = 5
re = solution(N, K)
print(re)
#=> -1

N = 100
K = 5
re = solution(N, K)
print(re)
#=> 10

N = 100
K = 7
re = solution(N, K)
print(re)
#=> 25

N = 1000
K = 12
re = solution(N, K)
print(re)
#=> 125


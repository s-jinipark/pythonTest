
# 프로그래머스 스타일 로 ...
def solution(N, K):
    answer = 0
    tmp = []
    # 약수 구하기
    for i in range(1, N+1):  # 자기 자신 포함
        #print(i)
        if N % i == 0:
            tmp.append(i)
    tmp.sort
    print(tmp)
    if len(tmp) < K or len(tmp) == 0:
        return -1
    answer = tmp[K-1]
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

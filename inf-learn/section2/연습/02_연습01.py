
##### K 번째 약수
def solution(N, K):
    answer = 0

    tmp = []
    for i in range(1, N+1):   # 1부터 시작한다는 점
        if N % i == 0 :   # 나머지 0 인 경우
            tmp.append(i)
    print(tmp)
    tmp.sort()
    # K 번째
    if len(tmp) < K :
        answer = -1
    else :
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

'''
풀이에서는 딱히 sort 안하고, 
약수 구하다가 K 번째되면 스톱...
'''

def solution(N):
    answer = 0
    # chk 배열 만들기
    chk = [False, False] + [True] *(N-1)  # 앞에 0, 1 이 False 로 빠짐
    primes = []

    for i in range(2, N+1):
        if chk[i] :
            primes.append(i)
            for j in range(i*2 , N+1, i):
                chk[j] = False
                #print(j, end=' ')
            #print()
    #print(primes)
    answer = len(primes)
    return answer

N = 20
re = solution(N)
print(re)
print('====================')
N = 2
re = solution(N)
print(re)  # => 1
print('====================')
N = 200000
re = solution(N)
print(re) # => 17984

print('====================')
N = 150000
re = solution(N)
print(re) # => 13848
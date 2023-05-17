
# 프로그래머스 스타일 로 ...

def solution(N):
    answer = 0
    # 배열 생성
    a = [False, False] + [True] * (N-1)
    primes = []
    print(a)

    for i in range(2, N+1):
        if a[i]:   # True
            primes.append(i)
            for j in range(2 * i, N + 1, i):
                print(j)
                a[j] = False

    print(primes)

    return answer


N=20

re = solution(N)
print(re)
#=>

'''
에라토스테네스의 체 : 범위에서 합성수를 지우는 방식으로 소수를 찾는 방법. 
1. 1은 제거 
2. 지워지지 않은 수 중 제일 작은 2를 소수로 채택하고, 나머지 2의 배수를 모두 지운다. 
3. 지워지지 않은 수 중 제일 작은 3을 소수로 채택하고, 나머지 3의 배수를 모두 지운다. 
4. 지워지지 않은 수 중 제일 작은 5를 소수로 채택하고, 나머지 5의 배수를 모두 지운다. 
5. (반복)

'''
def solution(n):
    answer = 0
    chk = []

    for i in range(2, n+1):
        print(i)
        # 하나씩 확인
        tmp = True
        for j in range(2, i):
            print(i, j)
            if i % j == 0 :
                tmp = False
                break
        if tmp :
            answer += 1
            chk.append(i)
    print(chk)
    return answer

n = 5

re = solution(n)
print(re)

print("====================")

# 시간초과 떠서 안됨 => 에라토스테네스의 체  써야 함

A = [False, False] + [True] * (n-1)
print(A)
primes = []

for i in range(2, n+1):  # 여기도 2 부터 시작
    if A[i] :
        primes.append(i)
    for j in range(2*i , n+1, i): # 배수를 다 지움
        # 2*i 에서 시작하는 이유?
        A[j] = False
print(primes)


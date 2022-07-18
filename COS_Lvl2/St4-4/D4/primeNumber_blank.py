def func_a(primes):
    primes = [False for _ in range(100000)]
    primes[0] = primes[1] = True

    for i in range(2, len(primes), 1):
        if primes[i] == False:
            j = 2
            while j * i < len(primes):
                primes[j * i] = True
                j += 1

    return primes

def func_b(number):
    primeset = []
    tmp = ''
    for i in range(len(number)-1):
        for j in range(i+1, len(number)):
            if number[i] != '0':
                tmp = number[i]+number[j]

            if len(tmp) == 2 and int(tmp) not in primeset:
                primeset.append(int(tmp))
            tmp = ''

    return primeset

def solution(numbers):
    answer = 0
    primes =[]
    primes =  func_a(primes)  # 소수 배열 을 먼저 구하네
    perms = func_b(numbers)
    print(perms)
    # 소수 구분 ??
    for num in perms:
        if primes[num] == False :
            answer = answer
        else:
            answer = answer + 1

    return answer


num = "13547241671"
res = solution(num)
print(res)

num = "012"
res = solution(num)
print(res)

num = "92151"
res = solution(num)
print(res)


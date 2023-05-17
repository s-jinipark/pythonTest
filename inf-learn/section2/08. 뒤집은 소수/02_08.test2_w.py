import math

def reverse(x):
    rtn = ''
    while x > 0 :
        #print(x//10, x % 10)
        # 어차피 붙여야 되서 str 로
        tmp = x % 10
        if tmp >0 :
            rtn += str(tmp)
        x = x // 10

    return int(rtn)

def isPrime(x):
    # for i in range(2, x):
    #     if x % i == 0 :
    #         return False
    # 업그레이드
    for i in range(2, int(math.sqrt(x))+1):  # (기억해야 할) int 변환 후 + 1
        if x % i == 0 :
            return False
    return True

def solution(N, su):
    answer = 0
    r_list = []
    for s in su :
        print(s)
        rtn = reverse(s)
        print(rtn)
        print(isPrime(rtn))
        if isPrime(rtn) :
            r_list.append(rtn)
    print(r_list)
    return answer

N = 5
su = [32, 55, 62, 3700, 250]
re = solution(N, su)
print(re)
print('====================')

'''
https://seongonion.tistory.com/43

16을 예로 들어보자.

16의 약수들을 일렬로 나열하면 1, 2, 4, 8, 16이 된다.

중간값 4를 기준으로 양 옆을 보면 약수들이 서로 대칭되고 있음을 확인할 수 있다. (1 * 16 = 16 * 1, 2 * 8 = 8 * 2)

다시말해, 만약 우리가 16의 약수를 찾고 싶다면 16의 약수의 중간값을 기준으로 
한 쪽만 검사를 하더라도 다른 쪽의 약수들을 알 수 있다.

여기서 중간값은 찾고자하는 수의 제곱근 값으로 가정해 처리할 수 있으며,
이 제곱근 값을 기준으로 왼쪽에 약수가 하나도 존재하지 않는다면 
제곱근 값 기준 오른쪽에도 약수가 존재하지 않는다고 확신할 수 있다.

이를 통해 우리는 기존 for문이 2에서 N-1까지 돌았던 것을 
2에서 N의 제곱근까지만 돌도록 처리해주어 연산 횟수를 절반에 가깝게 줄여줄 수 있다.

이 방식으로 접근했을 때 작성한 코드는 다음과 같다.

# 제곱근을 구하기 위해 math 라이브러리 임포트
import math

def is_prime_num(n):
    for i in range(2, int(math.sqrt(n))+1): # n의 제곱근을 정수화 시켜준 후 + 1
        if n % i == 0:
            return False

    return True


==============================

[2부터 n-1까지 나누기]

def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False  
    return True
    
n-1까지, n이 1과 자기 자신 외의 수로 나누어지는지 판단하는 알고리즘이다. 
만약 나누어진다면 바로 false를 리턴한다. n-1까지 걸리지 않는다면 True가 리턴된다. 
가장 간단하고, 기초적이지만 오래 걸린다. 2부터 n-1까지의 수 모두를 확인하기 때문에, 시간 복잡도가 O(n)이다.


[n/2까지 나누기]

def isPrime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False  
    return True
    
n의 모든 약수는 n/2보다 작다. 고로 2부터 n-1까지 확인할 필요가 없다는 뜻이다. 
위 알고리즘보단 확인해야 할 조건이 반으로 줄었지만 여전히 시간 복잡도가 O(n)이기 때문에 느리다. 

 
[n의 제곱근까지 나누기]

def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False  
    return True
    
n의 제곱근을 기준으로, 제곱근보다 작은 수들 중에 약수가 없다면, 제곱근보다 큰 수들은 n의 약수가 아니다. 
예를 들어 n이 101이라면, √101+1까지의 수만 약수인지 확인해보면 된다. 

만약 n/2 알고리즘을 쓰면 101//2+1 = 51, 즉 2~51까지 50번을 확인해야 하지만, 
n의 제곱근까지만 확인하면 √101+1 = 11, 즉 2~11까지 총 10번만 하면 된다. 
그래서 시간 복잡도는 O(√n)으로, 1번의 방법들 중 제일 빠른 방법이다.

'''
#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(a, b):
    # 여기에 코드를 작성해주세요.
    answer = 0
    check = [False, False] + [True] * (b - 1)
    #print(check)  # [False, False, True, ... -> 앞 두개만 False, 나머진 True
    primes = []

    for i in range(2, b + 1):
        if check[i]:
            primes.append(i)
            print(i)
            for j in range(2 * i, b + 1, i):   # 배수들을 모두 False 로
                check[j] = False
                print('>', j)
    print(primes)
    for v in primes:
        t1 = v ** 2
        t2 = v ** 3
        if a<= t1 <= b:
            answer += 1
        if a<= t2 <= b:
            answer += 1

    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
a =  6
b =  30
ret = solution(a, b)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")


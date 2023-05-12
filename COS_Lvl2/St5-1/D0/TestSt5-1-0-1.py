
# 재귀함수

def factorial(n):
    if n <= 1 :
        return 1
    #return n * factorial(n-1)
    # [2] 중간 과정을 보기 위해
    tmp = factorial(n-1)
    print( n, ' * ', tmp, ' = ',  n * tmp )
    return n * tmp

print(factorial(5))

'''
재귀함수란 자기 자신을 다시 호출하는 함수를 의미한다.

재귀함수는 종료 조건을 명시하지 않으면, 자기 자신을 무한대로 호출하기 때문에 종료 조건을 반드시 설정해야 한다.

재귀함수의 대표적인 예제로는 팩토리얼(factorial) 이 있다.


그래서
5 * factorial(4)
5 * 4 * factorial(3)
5 * 4 * 3 * factorial(2)
5 * 4 * 3 * 2 * factorial(1)
이런 식으로 되겠지

'''



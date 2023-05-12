import math

def solution(n, m):
    answer = []
    print(math.gcd(n,m))
    print(math.lcm(n,m))
    answer.append(math.gcd(n,m))
    answer.append(math.lcm(n,m))
    return answer

n = 3
m = 12

re = solution(n, m)
print(re)

print("====================")

'''
최대 공약수 란
  GCD (Greatest Common Divisor)
  두 수 혹은 그 이상의 여러 수의 공통인 약수 중, 최대인 것
  8 의 약수 : 1, 2, 4, 8
  10의 약수 : 1, 2, 5, 10
  최대 공약수는 2
  
최소 공배수 란
  LCM (Least Common Multiple)
  두 수, 혹은 그 이상의 수들의 공통인 배수 중 최소
  즉, 수 들의 각각의 배수 중 공통이며 가장 작은 수
  10의 배수 : 10,20,30,40,50,60,70, ...
  12의 배수 : 12,24,36,48,60,72, ...
  최소 공배수는 60  

'''
a = 3
b = 12

# 최대 공약수
for i in range(min(a,b), 0, -1):
    if a % i == 0 and b % i == 0 :   # i 가 적어지므로 i 로 나눈다는 ...
        print(i)
        break

# 최소 공배수
for i in range(max(a,b), (a*b)+1):
    if i % a == 0 and i % b == 0 :   # i 가 커지므로 a,b 로 나눈다는 ...
        print(i)
        break

# 유크리드 호제법 (참조 : https://codingpractices.tistory.com/34)
# 계속해서 x 에는 y 값을 대입하고, y 에는 (x % y)값인 r 을 대입 하다보면
# x % y = 0 일 때가 있고 이 때, y 가 최대 공약수

def GCD(x, y):
    while(y):  # y가 참 일 동안 = 자연수일 때
        x, y = y, x % y
    return x

def LCM(x, y):
    result = (x * y) // GCD(x, y)
    return result

print( GCD(a, b) )
print( LCM(a, b) )


import sys

sys.stdin = open("input_042.txt", "rt")

'''
두 자연수 A 와 B 가 있을 때 A의 배수이면서 B의 배수인 자연수를 
A와 B의 공배수라고 한다
이 중 가장 작은 수를 최소 공배수라고 한다

[1] 유클리드 호제법
   gcd (6, 10)
10 % 6 = 4
     6 % 4 = 2
         4 % 2 = 0
         
MOD 결과 값이 0 이 나오면, 그 연산의 작은 수를 최대 공약수로 선택

[2] 두 수의 곱을 최대 공약수로 나눈 값
    -> 최소 공배수
    
'''

def gcd(a, b):
    print('>', a, b)
    if b == 0 :
        return a
    else :
        return gcd(b, a % b)  # 재귀 형태

T  = int(input())
print(T)

for i in range(T):
    a, b = map(int, input().split())
    print(gcd(a, b))
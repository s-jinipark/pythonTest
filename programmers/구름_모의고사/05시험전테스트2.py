
# math.gcd() 함수를 이용하면 최대공약수(gcd, greatest common divisor)를 쉽게 구할 수 있다.
# math.gcd() 함수는 파이썬 3.5 버전부터 사용할 수 있다.
# 파이썬 3.9 버전부터는 math.gcd의 인수로 여러개가 가능하지만 3.9 미만 버전에서는 2개까지만 허용된다.

import math

test = math.gcd(60, 100, 80)
print(test)

# 2개씩 한다면
test2 = math.gcd(100,80)
print(test2)
test3 = math.gcd(test2, 60)
print(test3)


# 결과 => 20
'''
어린이집에서 사탕 60개, 초콜릿 100개, 젤리 80개를 준비했다. 
아이들이 서로 싸우지 않도록 똑같이 나누어 봉지에 담는다고 하면 최대 몇 봉지까지 만들 수 있을까?

math.gcd() 함수로 최대공약수를 구했더니 20이었다. 따라서 최대 20봉지를 만들 수 있다. 
각 봉지에 들어가는 사탕, 초콜릿, 젤리의 개수는 다음과 같이 전체 개수를 최대공약수 20으로 나누면 구할 수 있다.

>>> 60/20, 100/20, 80/20
(3.0, 5.0, 4.0)

'''

#--------------------------------------------------
print('--------------------')
# LCM = n1 * n2 / GCD

# math.lcm()은 최소공배수(lcm, least common multiple)를 구하는 함수이다.
# math.lcm() 함수는 파이썬 3.9 버전부터 사용할 수 있다.

t = math.lcm(15, 25)
print(t)

# 만약 없다면
t2 = math.gcd(15,25)
print(t2)
t3 = 15*25/t2
print(t3)

'''
어느 버스 정류장에 시내버스는 15분마다 도착하고 마을버스는 25분마다 도착한다고 한다. 
오후 1시에 두 버스가 동시에 도착했다고 할 때 두 버스가 동시에 도착할 다음 시각을 알려면 어떻게 해야 할까?


https://wikidocs.net/106253

math.lcm() 함수를 사용하여 최소공배수 75를 구했다. 따라서 두 버스가 동시에 도착할 다음 시각은 75분 후인 오후 2시 15분이다.

'''

#--------------------------------------------------
print('--------------------')

# 약수 구하기
# [Algorithm/Python] 파이썬 약수 구하기 (시간복잡도 줄여보기)
# https://minnit-develop.tistory.com/16


def getMyDivisor(n):

    divisorsList = []

    for i in range(1, n + 1):
        if (n % i == 0) :
            divisorsList.append(i)

    return divisorsList

print(getMyDivisor(10))

#2.2. 더 효율적인 풀이 방법

def getMyDivisor2(n):
    divisorsList = []

    for i in range(1, int(n ** (1 / 2)) + 1):  # 항상 약수를 구하면 그 짝이 되는 수가 존재한다.
        if (n % i == 0):   # N의 제곱근까지의 약수를 구하면 그 짝이 되는 약수는 자동으로 구할 수 있다.
            divisorsList.append(i)
            if ((i ** 2) != n):
                divisorsList.append(n // i)

    divisorsList.sort()

    return divisorsList

print(getMyDivisor2(10))


#--------------------------------------------------
print('--------------------')

a = [(1, 2), (5, 1), (0, 1), (5, 2), (3, 0)]
# key 인자를 정하지 않은 기본적인 sort에선, 튜플 순서대로 우선순위 기본 할당
b = sorted(a)
print(b)

# key 인자에 함수를 넘겨주면 우선순위가 정해짐.
c = sorted(a, key= lambda x : x[0])
print(c)
d = sorted(a, key= lambda x : x[1])
print(d)

# 비교할 아이템이 요소가 복수 개일 경우, 튜플로 우선순위를 정해줄 수 있다.
e = sorted(a, key = lambda x : (x[0], -x[1]))
print(e)
# [(0, 1), (1, 2), (3, 0), (5, 2), (5, 1)]
e2 = sorted(a, key = lambda x : (x[0], x[1]))
print(e2)
# => https://gorokke.tistory.com/38

'''
key = lambda 사용법
이중 리스트일 때, key에 lambda를 사용하여 정렬 기준을 설정할 수 있다.

람다식은 lambda 인자 : 표현식 형태로 사용한다.
아래 사용된 key=lambda x : x[0] 는 아래 코드와 같다.

def lambda(x):
  return x[0] 

(참조) https://velog.io/@sloools/Python3-%EC%A0%95%EB%A0%AC-%EB%9E%8C%EB%8B%A4-keylambda
'''

#list[0]를 기준으로 정렬
list_1 = [[3, 'three'],[4, 'four'],[2, 'two'],[1, 'one']]
print(sorted(list_1, key=lambda x : x[0]))
#출력 : [[1, 'one'], [2, 'two'], [3, 'three'], [4, 'four']]

# 문자열의 길이를 기준으로 정렬
list_2 = ['my', 'name', 'is', 'song']
print(sorted(list_2, key=lambda x : len(x)))
# 출력 : ['is', 'my', 'name', 'song']
print(sorted(list_2, key=lambda x : -len(x)))

'''
https://daeun-computer-uneasy.tistory.com/74?category=983126

[알고리즘] 특정 기준으로 리스트 정렬하기 (python) - key=lambda

# key가 하나일 때 
모든 정렬의 기반은 오름차순 정렬이다. 

ex 1) 리스트의 각 원소를 기준으로 정렬하기 (일반 오름차순) 
참고로 문자열을 다음과 같이 정렬하면 사전순으로 정렬이 된다. 

arr = ['abc', 'bac', 'bca']
sorted(arr, key=lambda x : x)
 

ex 2) 리스트 각 원소의 첫글자를 기준으로 정렬하기
리스트의 각 원소를 x로 받는다고 가정하면 다음과 같이 정렬할 수 있다. 

arr = ['abc', 'bac', 'bca']
sorted(arr, key=lambda x : x[0])
'''
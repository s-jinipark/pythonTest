
# 코드 암기 필요
# (Greatest Common Divisor, GCD)
def gcd (a, b) :
    while b != 0 :
        r = a % b  # 나머지 값 -> r
        a = b
        b = r
    return a

# 최소공배수(Least common multiple)
def lcm(a, b) :
    return a*b // gcd(a, b)  # 필요한 건 몫

def solution(numlist):
    answer = 0
    # 코드를 작성하세요.

    LCM = numlist[0]

    for i in range(1, len(numlist)) :
        LCM = lcm(LCM, numlist[i])
        #print(LCM)
    answer = LCM
    return answer

'''
공통으로 들어 있는 배수를 찾을 것이고
가장 먼저 오는 녀석 이니까 '최소 공배수'

함께 알아 둘 것
약수 중 가장 큰 값 -> 최대 공약수

a, b 자연수 (a > b)
r = a % b 나머지 값 

'''


numlist = [6, 8, 5, 12]
res = solution(numlist)
print(res)

# numlist = [4, 7, 20, 12]
# res = solution(numlist)
# print(res)


def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
        #print(a,b,r)

    return a


def lcm(a, b):
    return a*b//gcd(a, b)


arr = [10, 30, 20, 10]

answer = gcd(arr[0], arr[1])
for i in range(2, len(arr)):
    answer = gcd(answer, arr[i])
print(answer)

'''
과일의 종류가 4개 , 개수는 제각각
일정 봉투에 (일정 갯수) 공평 분배
모든개 맞아 떨어지진 않지만
몇개 봉투가 나올 수 있다는 됨
=> 최대 공약수 ??
'''


# arr = [25, 40, 60]
# answer = gcd(arr[0], arr[1])
# for i in range(2, len(arr)):
#     answer = gcd(answer, arr[i])
# print(answer)
#
#
# arr = [15, 55, 20, 30, 40]
# answer = gcd(arr[0], arr[1])
# for i in range(2, len(arr)):
#     answer = gcd(answer, arr[i])
# print(answer)


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

어린이집에서 사탕 60개, 초콜릿 100개, 젤리 80개를 준비했다. 
아이들이 서로 싸우지 않도록 똑같이 나누어 봉지에 담는다고 하면 최대 몇 봉지까지 만들 수 있을까?

'''



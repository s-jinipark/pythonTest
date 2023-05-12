def gcd(a, b):
    while b != 0 :
        r = a % b
        a = b
        b = r
    return a

def lcm(a, b):
    return a*b // gcd(a, b)

arr = [10, 15, 20, 10]
answer = lcm(arr[0], arr[1])
for i in range(2, len(arr)):
    answer = lcm(answer, arr[i])
print(answer)

'''
달리기를 가정
어떤사람은 10m, 15m 간다..
트랙을 돈다고 할 때, 어느 순간에 만나는 지점??
=> 최소 공배수 문제

버스들이 출발
10분단위, 15분 단위...
함께 출발하는 시간

'''

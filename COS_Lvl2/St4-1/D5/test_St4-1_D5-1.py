
def gcd( a, b ):
    while b !=0 :
        r = a%b
        a = b
        b = r
    return a

def lcm(a, b):
    return a*b//gcd(a,b)

arr = [10, 30, 20, 10]

answer = gcd(arr[0], arr[1])
for i in range(2, len(arr)):
    answer = gcd(answer, arr[i])
print(answer)  # 10


arr = [10, 15, 20, 10]
answer = lcm(arr[0], arr[1])
for i in range(2, len(arr)):
    answer = lcm(answer, arr[i])
print(answer)  # 60

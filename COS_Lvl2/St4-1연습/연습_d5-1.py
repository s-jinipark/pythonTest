def gcd(a, b):
    while b != 0 :
        r = a % b  # 나머지
        print('r, a, b ->', r, a, b)
        a = b
        b = r
        #print('r, a, b ->', r, a, b)
    return a


def lcm(a, b):
    return a*b//gcd(a, b)  # 몫


a = 8
b = 4
res1 = gcd(a, b)
res2 = lcm(a, b)
print("gcd =", res1, "lcm =", res2)


a = 4
b = 14
res1 = gcd(a, b)
res2 = lcm(a, b)
print("gcd =", res1, "lcm =", res2)

print('--------------------')
import math
a = 8
b = 4
res1 = math.gcd(a, b)
res2 = math.lcm(a, b)
print("gcd =", res1, "lcm =", res2)

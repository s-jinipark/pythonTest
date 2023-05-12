#test=[ int(input()) for _ in range(3)]
#print(test)

#a, b, c = map(int, input().split())
#a, b, c = 1000, 70, 170
# a, b, c = 3, 2, 1
# print(a, b, c)
#
# sum_ab = a
# sum_c = 0
# cnt = 0
#
# while sum_ab >= sum_c :
#     sum_ab += b
#     sum_c += c
#     cnt += 1
#     if sum_ab >  2100000000 :
#         cnt = -1
#         break
#
# print(sum_ab, sum_c, cnt)

#n = int(input())

# def factorial(n) :
#     if n <=1 :
#         return 1
#     return n * factorial(n-1)
#
# ans = factorial (n)
# print(ans)

def fibo(n):
    if n <= 0 :
        return 0
    if n == 1 :
        return 1
    return fibo(n-1) + fibo(n-2)

ans = fibo(10)
print(ans)


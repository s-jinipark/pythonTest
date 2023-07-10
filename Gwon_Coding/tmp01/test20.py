
# 여기서부터는 몇 번인지 적어 주자
# 팩토리얼 연습_tmp

# def factorial(n):
#     if n < 1 :
#         return 1
#     return n * factorial(n-1)
#
# tot = factorial(5)
# print(tot)


# 피보나치
# def fibo(n):
#     if n == 0 :
#         return 0
#     if n == 1 :
#         return 1
#     # 2부터 임
#     return fibo(n-1) + fibo(n-2)
#
# tot = fibo(5)
# print(tot)


# 재귀함수가 뭔가요?
def recursive(n):
    if n == 0 :
        return
    print('앞')
    recursive(n-1)
    print('뒤')

recursive(3)

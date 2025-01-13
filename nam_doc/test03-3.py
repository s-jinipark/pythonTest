
#입력한 숫자가 소수인지

while True:
    num = input("2 이상의 숫자를 입력하세요> ")

    if not num.isnumeric:
        continue
    num = int(num)
    if num < 2:
        continue
    break

# isprime = True
# for n in range(2, num):
#     if num % n == 0:
#         isprime = False
#         break

# if isprime:
#     print("소수 입니다.")
# else:
#     print("소수가 아닙니다.")


#다른 방법
#에라토스테네스의 체
# ->  이 방법은 마치 체로 치듯이 수를 걸러낸다고 하여 ..
prime_list = [False, False] + [True] * (num -1)
# => False, False, True, True, ... 로 셋팅(3번째 부터 True)
primes = []

for i in range(2, num+1):
    if prime_list[i]:  #[i 가 소수인 경우]
        for j in range(2*i, num+1, i): 
            prime_list[j] = False  #[# i 이후 i의 배수들을 False 판정]

primes = [i for i in range(2, num+1) if prime_list[i]==True]
#[True 인 것만 ...]
print(primes)

if num in primes:
    print("소수 입니다.")
else:
    print("소수가 아닙니다.")


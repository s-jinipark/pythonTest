
# N ! 를 출력하는 프로그램을 작성하시오
# 0 < N < 12 가 주어 진다
#   =   =

N = 6
sum = 1

for i in range(1,N+1):
    print(i)
    sum *= i
print("sum: " , sum)


# --------------------

sum2 = 0

def fact(N):

    if (N > 1) :
        return N * fact(N-1)
    else :
        return 1

sum2 = fact(N)
print(sum2)

# --------------------
# 연습

def fac(n):
    if n == 1 :
        return  1
    else :
        return n * fac(n-1)

sum3 = fac(N)
print(sum3)
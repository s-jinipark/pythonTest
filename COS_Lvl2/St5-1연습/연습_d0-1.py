
def factorial(n):
    if n <= 1 :
        return 1

    tmp = factorial(n-1)
    #print(tmp)
    return n * tmp

print(factorial(5))


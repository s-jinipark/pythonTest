

def factorial(n):
  if n == 0 or n == 1:
    return 1
  else:
    return factorial(n-1)

def solution(male, female):
    print(factorial(male), factorial(male +female), factorial(female) )
    return factorial(male) // (factorial(male - female) * factorial(female))

'''

'''
male =5
female =2

an = solution(male, female)
print(an)

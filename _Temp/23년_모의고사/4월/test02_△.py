
# 숫자 채우기

answer = [[]]

def func_a(n):
    num = 1
    for i in range(n):
        for j in range(i+1):  # <- *
            answer[i][j] += num
            num += 1

def func_b(n):
    num = 1
    for i in range(n):
        for j in range(n-i):
            answer[i][j] += num
            num += 1

def func_c(n):
    num = 1
    for i in range(n):
        for j in range(n):
            if n-i-1 <= j :
                answer[i][j] += num
                num += 1

def func_d(n):
    num = 1
    for i in range(n):
        for j in range(n):
            if  j >= i :
                answer[i][j] += num
                num += 1

def print_buti(a):
    for i in range(n):
        for j in range(n):
            print(a[i][j] , end=' ')
        print()

def solution(n):
    global answer
    answer = [[0 for col in range(n)] for row in range(n)]

    func_a(n)
    #print_buti(answer)
    func_b(n)
    #print_buti(answer)
    func_c(n)
    #print_buti(answer)
    func_d(n)
    print_buti(answer)

    return answer

'''
시간 너무 오래 걸림

'''

n = 3
result = [[3, 4, 7], [6, 14, 8], [14, 10, 18]]

an = solution(n)
print(an)
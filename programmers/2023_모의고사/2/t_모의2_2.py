answer = [[]]


def func_a(n):
    num = 1
    for i in range(n):
        for j in range( i+1 ):
            answer[i][j] += num
            num += 1
    print(answer)

def func_b(n):
    num = 1
    for i in range(n):
        for j in range( n-i ):
            answer[i][j] += num
            num += 1
    print(answer)

def func_c(n):
    num = 1
    for i in range(n):
        for j in range(n):
            #if n + i >= j:
            #if i >= j :
            print(n - i - 1)  # 2-> 1-> 0 을 만들어 주면 되는데...
            if j >= n - i - 1:  # 이게 생각 안남...
                answer[i][j] += num
                num += 1
    print(answer)

def func_d(n):
    num = 1
    for i in range(n):
        for j in range(n):
            if i <= j :
                answer[i][j] += num
                num += 1
    print(answer)

def solution(n):
    global answer
    answer = [[0 for col in range(n)] for row in range(n)]

    #func_a(n)
    #func_b(n)
    func_c(n)
    #func_d(n)

    return answer

n = 3
schedule = [[3,4,7], [6,14,8], [14,10,18]]

solution(n)

def solution(n):
    answer = 0
    Min = n
    for i in range(n, 1, -1):
        print(n % i)
        if n % i == 1 :
            print('>', i)
            if Min > i :
                Min = i
    answer = Min
    return answer

#n = 10
n = 12

re = solution(n)
print(re)

print("====================")


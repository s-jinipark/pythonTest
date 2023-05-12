def solution(a, b, n):
    answer = 0

    while n >= a:
        answer += (n//a) * b   #  b 가 들어가야 함?
        n = (n%a)+(n//a)*b  # b 가 꼭 들어 가는 군 

    return answer

a = 3
b = 1
n = 20
re = solution(a, b, n)
print(re)


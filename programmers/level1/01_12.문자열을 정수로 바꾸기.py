def solution(s):
    answer = 0
    sign = 1
    start = 0
    if s[0] == '-':
        sign = -1
        start = 1
    elif s[0] == '+':
        sign = 1
        start = 1

    answer = int(s[start:]) * sign

    return answer

s = '-1234'

re = solution(s)
print(re)

print("====================")


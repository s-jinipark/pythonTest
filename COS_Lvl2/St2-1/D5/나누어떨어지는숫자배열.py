# 나누어떨어지는숫자배열

def solution(arr, divisor):
    answer = []
    for a in arr :
        if a % divisor == 0 :
            answer.append(a)
    if len(answer) == 0 :
        answer.append(-1)
    return answer


# main 부분
# arr = [5, 9, 7, 10]
# divisor = 5      # [5, 10]

# arr = [2, 36, 1, 3]
# divisor = 1      # [1, 2, 3, 36]

arr = [3,2,6]
divisor = 10     # [-1]

res = solution(arr, divisor)
print(res)



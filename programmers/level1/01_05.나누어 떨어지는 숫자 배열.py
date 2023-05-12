def solution(arr, divisor):
    answer = []
    for a in arr :
        if a % divisor == 0 :
            answer.append(a)
    if answer :
        answer.sort()
    else :
        answer.append(-1)

    return answer

arr = [5, 9, 7, 10]
divisor = 5

re = solution(arr, divisor)
print(re)

print("====================")

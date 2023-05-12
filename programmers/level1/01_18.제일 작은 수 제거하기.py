def solution(arr):
    answer = []
    Min = min(arr)
    print(Min)

    # copy
    for i in range(len(arr)):
        if Min == arr[i]:
            continue
        answer.append(arr[i])

    if len(answer) == 0:
        answer.append(-1)
    return answer

#arr = [4,3,2,1]
arr = [10]

re = solution(arr)
print(re)

print("====================")


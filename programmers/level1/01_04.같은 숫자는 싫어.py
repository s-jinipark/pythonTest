def solution(arr):
    answer = []
    prev = -1
    for a in arr:
        if prev != a :
            answer.append(a)
            prev = a

    return answer


arr = [1,1,3,3,0,1,1]

re = solution(arr)
print(re)

print("====================")

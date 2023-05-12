def solution(array, commands):
    answer = []

    for i in commands:
        start = i[0] -1   # 주의 : -1
        end = i[1]
        k = i[2]
        print(start, end, k)
        print(array[start:end])
        tmp = array[start:end]
        tmp.sort()
        print(array, tmp)
        answer.append(tmp[k-1])
    return answer


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

re = solution(array, commands)
print(re)

print("====================")

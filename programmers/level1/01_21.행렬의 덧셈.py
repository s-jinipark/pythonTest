def solution(arr1, arr2):
    answer = []  #[[]]
    print(len(arr1))
    for i in range(len(arr1)):
        tmp = []
        for j in range(len(arr1[0])):  # 행렬의 크기가 같다며
            tmp.append(arr1[i][j] + arr2[i][j])
        print(tmp)
        answer.append(tmp)
    return answer

arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]

re = solution(arr1, arr2)
print(re)

print("====================")

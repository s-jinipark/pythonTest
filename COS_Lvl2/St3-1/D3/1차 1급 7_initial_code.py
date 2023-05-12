def solution(arrA, arrB):
    arrA_idx = 0
    arrB_idx = 0
    arrA_len = len(arrA)
    arrB_len = len(arrB)
    answer = []
    #while @@@:
    while arrA_idx == arrB_idx:
        if arrA[arrA_idx] < arrB[arrB_idx]:
            answer.append(arrA[arrA_idx])
            arrA_idx += 1
        else:
            answer.append(arrB[arrB_idx])
            arrB_idx += 1
    #while @@@:
    while arrA_idx < arrA_len:
        answer.append(arrA[arrA_idx])
        arrA_idx += 1
    #while @@@:
    while arrB_idx < arrB_len:
        answer.append(arrB[arrB_idx])
        arrB_idx += 1
    answer.sort()
    return answer


#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
arrA = [-2, 4, 5, 9]
arrB = [1, 3, 10]
#arrA = [-2, 3, 5, 9]
#arrB = [0, 1, 5]
ret = solution(arrA, arrB)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("Solution: return value of the function is ", ret, " .")
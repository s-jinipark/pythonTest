
def solution(numbers):
    answer = []

    # 서로 다른 인덱스에 있는 두 개의 수를 뽑아
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            print(i, j, numbers[i], numbers[j] )
            tmp = numbers[i] + numbers[j]
            answer.append(tmp)
    tmp_set = set(answer)
    answer = list(tmp_set)   # 소트는 자동인 듯
    return answer

numbers = [2,1,3,4,1]

re = solution(numbers)
print(re)

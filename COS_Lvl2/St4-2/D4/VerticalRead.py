
def solution(sample):
    answer = ''
    tmp_2arr = [['' for _ in range(15)] for _ in range(5)]
    print(tmp_2arr)

    # 데이터 적재
    for i in range(5):
        for j in range(len(sample[i])):
            #print(sample[i][j])
            tmp_2arr[i][j] = sample[i][j]
    print(tmp_2arr)

    # 인쇄
    for i in range(15):
        for j in range(5):
            #print( tmp_2arr[j][i] )
            if tmp_2arr[j][i] != '' :
                answer += tmp_2arr[j][i]

    return answer



sample1 = ["ABCDE", "abcde", "01234", "FGHIJ", "fghij"]
res1 = solution(sample1)
print(res1)

sample1 = ["AABCDD", "afzz", "09121", "a8EWg6", "P5h3kx"]
res1 = solution(sample1)
print(res1)
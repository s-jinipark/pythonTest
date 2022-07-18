def solution(n, A):
    answer = ''
    tmp_180 = [[0 for _ in range(n)] for _ in range(n)]
    #print(tmp_180)
    # 회전
    for i in range(n):
        for j in range(n) :
            tmp_180[n-1-i][n-1-j] = A[i][j]
    print(tmp_180)

    # 덧셈
    for i in range(n):
        for j in range(n) :
            tmp_sum = tmp_180[i][j] + A[i][j]
            #print(tmp_sum%10)
            if tmp_sum >= 10 :
                tmp_180[i][j] = tmp_sum%10
            else :
                tmp_180[i][j] = tmp_sum
    print(tmp_180)

    # 읽기
    for i in range(n):
        for j in range(n) :
            if i % 2 == 0 :
                answer += str(tmp_180[i][j])
            else :
                answer += str(tmp_180[i][n - 1 - j])

    return answer


A = [[5, 4, 7],
     [1, 5, 4],
     [7, 6, 8]]
res = solution(len(A), A)
print(res)

A = [[2, 7, 11, 9],
     [13, 8, 12, 3],
     [31, 18, 5, 6],
     [7, 17, 14, 7]]

res = solution(len(A), A)
print(res)

'''
[0][0]  -> [2][2]
[0][1]     [2][1]
[0][2]     [2][0]

[1][0]     [1][2]
[1][1]     [1][1]
[1][2]     [1][0]

'''

# 문제 004 > 구간 합 구하기 2
# X 는 행, Y 는 열을 의미한다

inp1 = "4 3"
n, quizNo = map(int, inp1.split())
print(n, quizNo)  # 데이터의 개수, 질의 개수

# #A = []
# A = [[0] * (n+1)]
# # 입력 받을 경우
# for i in range(n):
#     A_row = [0] + [int(x) for x in input().split()]
#     A.append(A_row)
A = [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 3, 4, 5], [0, 3, 4, 5, 6], [0, 4, 5, 6, 7]]
print(A)

D = [[0] * (n+1) for _ in range(n+1)]
#print(D)

for i in range(1, n+1):
    for j in range(1, n+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]

print(D)

#구간을 입력 받는다
for i in range(quizNo):
    print(i+1, " /" , quizNo , "> ", end='')
    x1, y1, x2, y2 = map(int, input().split())
    print(x1, y1, x2, y2)
    print( D[x2][y2] - D[x2][y1-1] - D[x1-1][y2] + D[x1-1][y1-1] )

'''
**
https://castlerain.tistory.com/100
여기 설명 볼 것

'''
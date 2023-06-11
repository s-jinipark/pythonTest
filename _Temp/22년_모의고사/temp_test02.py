

arr = [
    [1, 0, 1, 1],
    [1, 0, 0, 1],
    [1, 2, 3, 1],
    [1, 0, 2, 1]
]

#dy = 2
#dx = 1
# [나는 x : 행 , y : 열 로 해왔는데...]
# 강사는 수학의 x축, y 측으로 함
dx = 2
dy = 1

# 위,아래,왼쪽,오른쪽의 합을 구하는 프로그램
sum = 0
sum += arr[dx - 1 ][dy]
sum += arr[dx + 1 ][dy]
sum += arr[dx][dy - 1]
sum += arr[dx][dy + 1]

print(sum)

# 위 코드를 for 문으로 구현
# for 문 탐색 기법 direct 탐색 - 방향배열탐색

d_x = [-1,1,0,0]
d_y = [0,0,-1,1]
sum = 0
for i in range(4):
    nx = dx + d_x[i]
    ny = dy + d_y[i]

    #sum += arr[nx][ny]
    # [2] 여기에 조건 추가
    if 0<=nx<4 and 0<=ny<4 :  # 범위 밖 거른다
        sum += arr[nx][ny]

print('sum2 : ', sum)

print('==============================')

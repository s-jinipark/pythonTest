def solution(table, num):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] == 1:
                posx = i
                posy = j

    for d in range(1, num + 1):
        for i in range(4):
            nx = posx + dx[i] * d
            ny = posy + dy[i] * d

            if 0 <= nx < N and 0 <= ny < N:
                table[nx][ny] = 1



N = 7
table = [[0 for _ in range(N)] for _ in range(N)]
table[3][2] = 1
num = 2
solution(table, num)

for arr in table:
    print(arr)







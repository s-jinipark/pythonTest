def solution(table, pos, num):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    posx = ord(pos[0]) - ord('0')
    posy = ord(pos[1]) - ord('a')
    table[posx][posy] == 1

    for d in range(1, num + 1):
        for i in range(4):
            nx = posx + dx[i] * d
            ny = posy + dy[i] * d

            if 0 <= nx < N and 0 <= ny < N:
                table[nx][ny] = 1



N = 9
table = [[0 for _ in range(N)] for _ in range(N)]
pos = "4e"
num = 2
solution(table, pos, num)

for arr in table:
    print(arr)







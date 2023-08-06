def solution(n, x, y):
    matrix = [[-1 for _ in range(n)] for _ in range(n)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    max_dist = 0

    q = []
    matrix[x][y] = 0   # -1 에서 0 으로..
    q.append((x, y))

    while len(q):
        cur_x, cur_y = q[0]
        q.pop(0)
        max_dist = max(max_dist, matrix[cur_x][cur_y])

        for i in range(0, 4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]
            if next_x < 0 or next_y < 0 or next_x >= n or next_y >= n:
                continue
            if matrix[next_x][next_y] == -1:
                #matrix[next_x][next_y] += 1
                matrix[next_x][next_y] = matrix[cur_x][cur_y] +1
                q.append((next_x, next_y))

    return max_dist + 3


an = solution(3, 1, 1)  # n, x, y   -> 3 * 3 크기의 땅의 (1, 1) 칸에 묻힌 쓰레기가 0일 차에 썩기 시작
print(an)
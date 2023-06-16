def solution(seats):
    answer = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    n = len(seats)
    visited = [[0] * 50 for _ in range(50)]

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and seats[i][j] == 1:
                answer += 1
                q = []
                q.append((i, j))
                visited[i][j] = 1

                while q:
                    cur = q.pop(0)

                    for k in range(4):
                        nx = cur[0] + dx[k]
                        ny = cur[1] + dy[k]
                        if nx < 0 or nx >= n or ny < 0 or ny >= n:
                            continue
                        if visited[nx][ny] == 1 or seats[nx][ny] == 1:
                            continue
                        visited[nx][ny] = 1
                        q.append((nx, ny))

    return answer


seats = [[1,1,0],[1,0,0],[0,0,1]]

ans= solution(seats)

print('ans:', ans)
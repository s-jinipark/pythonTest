
def solution(coloring):
    answer = []
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    n = len(coloring)
    visited = [[0] * 50 for _ in range(50)]

    def dfs(x, y):
        count = 1
        visited[x][y] = 1

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if visited[nx][ny] == 1 or coloring[nx][ny] == 0:
                continue
            count += dfs(nx, ny)

        return count

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and coloring[i][j] == 1:
                answer.append( dfs(i,j) )

    answer.sort()
    return answer

coloring = [[1,1,0,0],[1,1,0,1],[0,0,1,1],[1,0,0,0]]

re = solution(coloring)
print(re)
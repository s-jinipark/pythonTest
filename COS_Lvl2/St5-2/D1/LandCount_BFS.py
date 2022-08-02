def bfs(data, x, y):
    dx = [-1, 1, 0, 0]   # 상하
    dy = [0, 0 , -1, 1]  # 좌우
    q = []
    q.append((x, y))
    data[x][y] = 1  # 방문
    while len(q) > 0 :
        p = q.pop(0)
        x = p[0]
        y = p[1]
        for i in range(len(dx)) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(data) and 0 <= ny < len(data[0]) :
                if data[nx][ny] == 0 :
                    q.append((nx, ny))
                    data[nx][ny] = 1

def solution(data):
    cnt = 0
    for i in range(len(data) ) :
        for j in range(len(data[0])) :
            if data[i][j] == 0 :
                cnt += 1
                bfs(data, i, j)

    return cnt


def main():
    # sample 1
    data = [ [0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
               [0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
               [0, 0, 1, 0, 0, 1, 1, 1, 1, 0],
               [0, 1, 1, 1, 1, 0, 0, 0, 1, 0],
               [1, 1, 1, 0, 1, 0, 0, 0, 1, 0],
               [0, 0, 0, 0, 1, 1, 0, 1, 1, 1],
               [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]]
    #count = solution(data)
    #print(count)    # 6

    # sample 2
    data = [[1, 0, 1, 0, 1],
            [0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1],
            [0, 0, 0, 0, 0],
            [1, 0, 1, 1, 1]]
    count = solution(data)
    print(count)    # 1


    # sample 3
    data = [[0, 0, 1, 0, 1, 1],
            [1, 0, 1, 1, 0, 1],
            [0, 0, 1, 0, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [0, 0, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 1],
            [1, 0, 1, 0, 0, 1],
            [0, 1, 1, 0, 1, 1]]
    #count = solution(data)
    #print(count)    # 8

    # sample 4
    data = [[0, 1, 0, 0, 1, 0],
            [1, 0, 0, 0, 0, 1],
            [0, 0, 1, 0, 1, 1],
            [1, 1, 1, 0, 1, 1],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 1, 1],
            [1, 0, 1, 0, 0, 1],
            [0, 1, 1, 0, 1, 1]]
    #count = solution(data)
    #print(count)    # 5


if __name__ == "__main__":
    main()

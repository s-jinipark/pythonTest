

def solution(data):
    cnt = 0
    # 1 은 도로 , 0 은 길이 아니므로 갈 수 없는 곳
    #dx = [1, 0]  # 아래
    #dy = [0, 1]  # 우측 만 가능
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    x, y, dist = 0, 0, 0
    rows = len(data)
    cols = len(data[0])
    q = []
    q.append((x, y, dist))

    while len(q) > 0 :
        x, y, dist = q.pop(0)
        data[x][y] = 0

        if x == rows -1 and y == cols -1 :  # 부산 도착
            cnt = dist
            break

        for i  in range(len(dx)) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < rows and 0 <= ny < cols and data[nx][ny] == 1:
                q.append((nx, ny, dist + 1))

    return cnt


def main():
    # Sample 1
    road = [[1, 1, 1, 1, 1, 1],
            [0, 0, 1, 0, 0, 1],
            [1, 1, 1, 0, 1, 1],
            [1, 0, 0, 0, 1, 0],
            [1, 1, 1, 0, 1, 0],
            [0, 0, 1, 1, 1, 1]]

    # Sample 2
    # road = [[1,1,1,0,0,1,1,1,1],
    #         [0,0,1,1,1,1,1,1,1],
    #         [0,0,1,1,1,0,0,0,1],
    #         [0,0,1,0,1,0,0,0,1],
    #         [0,0,1,0,1,1,0,0,1],
    #         [0,0,1,0,0,1,1,0,1],
    #         [0,0,1,0,0,0,1,1,1],
    #         [0,0,1,1,1,1,1,1,1]]

    result = solution(road)
    print(result)

if __name__ == "__main__":
    main()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(arr , x, y) :
    arr[x][y] = 1

    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < len(arr) and 0 <= ny < len(arr[0]):
            if arr[nx][ny] == 0 :
                dfs(arr, nx, ny)

def solution(data):
    cnt = 0

    arr = data

    for i in range(len(data)):
        for j in range(len(data[0])) :
            if arr[i][j] == 0 :
                cnt += 1
                dfs(data, i, j)

    return cnt


def main():
    # sample 1
    data = [   [0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
               [0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
               [0, 0, 1, 0, 0, 1, 1, 1, 1, 0],
               [0, 1, 1, 1, 1, 0, 0, 0, 1, 0],
               [1, 1, 1, 0, 1, 0, 0, 0, 1, 0],
               [0, 0, 0, 0, 1, 1, 0, 1, 1, 1],
               [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]]
    count = solution(data)
    print(count)    # 6

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

def solution(row, col):
    result = [[0 for _ in range(col)] for _ in range(row)]
    num = 1

    for c in range(col - 1, -1, -1):
        if (col % 2 == 1 and c % 2 == 0) or (col % 2 == 0 and c % 2 == 1):
            for r in range(row - 1, -1, -1):
                result[r][c] = num
                num+=1

        else:
            for r in range(0, row):
                result[r][c] = num
                num+=1

    return result




def main():
    r = 6
    c = 5
    ary = solution(r, c)
    print(ary)

if __name__ == "__main__":
    main()


# r = D5, c = D5 인 경우
# [[25, 16, 15, 6, D5],
#  [24, 17, 14, 7, 4],
#  [23, 18, 13, 8, 3],
#  [22, 19, 12, 9, 2],
#  [21, 20, 11, 10, 1]]


# r = 6, c = D5 인 경우
# [[30, 19, 18, 7, 6],
#  [29, 20, 17, 8, D5],
#  [28, 21, 16, 9, 4],
#  [27, 22, 15, 10, 3],
#  [26, 23, 14, 11, 2],
#  [25, 24, 13, 12, 1]]








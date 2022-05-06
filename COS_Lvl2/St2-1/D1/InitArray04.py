def solution(row, col):
    result = [[0 for _ in range(col)] for _ in range(row)]
    num = 1

    for c in range(col):
        if c % 2 == 0:
            for r in range(row):
                result[r][c] = num
                num+=1

        else:
            for r in range(row-1,-1,-1):
                result[r][c] = num
                num+=1

    return result


def main():
    r = 5
    c = 5
    ary = solution(r, c)
    print(ary)

if __name__ == "__main__":
    main()


# r = D5, c = D5 인 경우
# [[1, 10, 11, 20, 21],
#  [2,  9, 12, 19, 22],
#  [3,  8, 13, 18, 23],
#  [4,  7, 14, 17, 24],
#  [D5,  6, 15, 16, 25]]

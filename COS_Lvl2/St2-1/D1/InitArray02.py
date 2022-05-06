def solution(row, col):
    result = [[0 for _ in range(col)] for _ in range(row)]
    num = 1

    for c in range(col):
        for r in range(row):
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
# [[1,  6, 11, 16, 21],
#  [2,  7, 12, 17, 22],
#  [3,  8, 13, 18, 23],
#  [4,  9, 14, 19, 24],
#  [D5, 10, 15, 20, 25]]

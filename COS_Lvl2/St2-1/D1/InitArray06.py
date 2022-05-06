def solution(row, col):
    result = [[0 for _ in range(col)] for _ in range(row)]
    num = 1

    for r in range(row - 1, -1, -1):
        if (row % 2 == 1 and r % 2 == 0) or (row % 2 == 0 and r % 2 == 1):
            for c in range(col - 1, -1, -1):
                result[r][c] = num
                num+=1

        else:
            for c in range(0, col):
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







# 홀수 행으로 이뤄진 경우
# [25, 24, 23, 22, 21]
# [16, 17, 18, 19, 20]
# [15, 14, 13, 12, 11]
# [ 6,  7,  8,  9, 10]
# [ D5,  4,  3,  2,  1]

# 짝수 행으로 이뤄진 경우
# [26, 27, 28, 29, 30]
# [25, 24, 23, 22, 21]
# [16, 17, 18, 19, 20]
# [15, 14, 13, 12, 11]
# [ 6,  7,  8,  9, 10]
# [ D5,  4,  3,  2,  1]

def solution(row, col):
    result = [[0 for _ in range(col)] for _ in range(row)]
    num = 1

    for r in range(row):
        for c in range(col):
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
# [[ 1,  2,  3,  4,  D5],
#  [ 6,  7,  8,  9, 10],
#  [11, 12, 13, 14, 15],
#  [16, 17, 18, 19, 20],
#  [21, 22, 23, 24, 25]]
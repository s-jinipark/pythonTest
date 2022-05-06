def solution(row, col):
    result = [[0 for _ in range(col)] for _ in range(row)]
    num = 1

    for r in range(row - 1, -1, -1):
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
# [[25, 24, 23, 22, 21],
#  [20, 19, 18, 17, 16],
#  [15, 14, 13, 12, 11],
#  [10,  9,  8,  7,  6],
#  [ D5,  4,  3,  2,  1]]
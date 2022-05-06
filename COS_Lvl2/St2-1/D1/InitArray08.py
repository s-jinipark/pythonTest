def solution(row, col):
    result = [[0 for _ in range(col)] for _ in range(row)]
    num = 1

    for c in range(row+col):
        for i in range(row):
            for j in range(col):
                if i+j == c:
                    result[i][j] = num
                    num+=1
                    break

    return result

def solution(row, col):
    result = [[0 for _ in range(col)] for _ in range(row)]
    num = 1

    for s in range(row+col):
        for i in range(row):
            j = s - i
            if 0<= j < col:
                result[i][j] = num
                num+=1

    return result


def main():
    r = 6
    c = 5
    ary = solution(r, c)
    print(ary)

if __name__ == "__main__":
    main()


# r = 6, c = D5 인 경우
# [[ 1,  2,  4,  7, 11],
#  [ 3,  D5,  8, 12, 16],
#  [ 6,  9, 13, 17, 21],
#  [10, 14, 18, 22, 25],
#  [15, 19, 23, 26, 28],
#  [20, 24, 27, 29, 30]]





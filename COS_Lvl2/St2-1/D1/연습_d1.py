
def solution1(row, col) :
    num = 1
    res = []
    for i in range(row) :
        tmp = [0] * col
        res.append(tmp)
    #print(res)
    for i in range(row):
        for j in range(col) :
            res[i][j] = num
            num += 1
    return res

def solution2(row, col) :
    num = 1
    res = []
    for i in range(row) :
        tmp = [0] * col
        res.append(tmp)
    #print(res)
    for i in range(row):
        for j in range(col) :
            res[j][i] = num
            num += 1
    return res

def solution3(row, col) :
    num = 1
    res = []
    for i in range(row) :
        tmp = [0] * col
        res.append(tmp)
    #print(res)
    for i in range(row):
        for j in range(col) :
            if i % 2 == 0 :  # 짝수
                res[i][j] = num
            else :
                res[i][col - 1 - j] = num
            num += 1
    return res

def solution4(row, col) :
    num = 1
    res = []
    for i in range(row) :
        tmp = [0] * col
        res.append(tmp)
    #print(res)
    for i in range(row):
        for j in range(col) :
            if i % 2 == 0 :  # 짝수
                res[j][i] = num
            else :
                res[row -1 - j][i] = num
            num += 1
    return res

def solution5(row, col) :
    num = 1
    res = []
    for i in range(row) :
        tmp = [0] * col
        res.append(tmp)
    #print(res)
    for i in range(row):
        for j in range(col) :
            res[row-1-i][j] = num
            num += 1
    return res

def solution6(row, col) :
    num = 1
    res = []
    for i in range(row) :
        tmp = [0] * col
        res.append(tmp)
    #print(res)
    for i in range(row):
        for j in range(col) :
            if i % 2 == 0:  # 짝수
                res[row - 1 - i][col -1 - j] = num
            else :
                res[row-1-i][j] = num
            num += 1
    return res

def solution7(row, col) :
    num = 1
    res = []
    for i in range(row) :
        tmp = [0] * col
        res.append(tmp)
    #print(res)
    for i in range(row):
        for j in range(col) :
            if i % 2 == 0 :  # 짝수
                res[row -1 - j][col-1-i] = num
            else :
                res[j][col-1-i] = num
            num += 1
    return res

def solution8(row, col) :
    num = 1
    res = []
    for i in range(row) :
        tmp = [0] * col
        res.append(tmp)
    #print(res)
    for s in range(row+col) :   # 사선의 갯수
        for i in range(row):
            for j in range(col) :
                if i+j == s :
                    res[i][j] = num
                    num += 1
    return res

def print1(row, col, arr):
    for i in range(row):
        for j in range(col) :
            print(arr[i][j], end=' ')
        print()

def main() :
    print('이차원 리스트 활용')
    r = 5
    c = 5
    ary = solution1(r, c)   # 일반적인 좌->우, 좌->우, ...
    print1(r, c, ary)
    print()
    ary = solution2(r, c)   # 상->하, 상->하, ...
    print1(r, c, ary)
    print()
    ary = solution3(r, c)   # 3. 좌->우, 우->좌, 번갈아 ...
    print1(r, c, ary)
    print()
    ary = solution4(r, c)   # 4. 상->하, 하->상, 번갈아 ...
    print1(r, c, ary)
    print()
    ary = solution5(r, c)   # D5. 좌->우, 좌->우,  인데 아래서 부터 ...
    print1(r, c, ary)
    print()
    ary = solution6(r, c)   # 6. 우->좌, 좌->우,  아래서 부터 번갈아 ...
    print1(r, c, ary)
    print()
    ary = solution7(r, c)   # 7. 하->상, 상->하,  우측 부터 번갈아 ...
    print1(r, c, ary)
    # 8. 사선으로 => 풀이 보고 코딩함
    print()
    ary = solution8(r, c)
    print1(r, c, ary)

if __name__ == '__main__' :
    main()
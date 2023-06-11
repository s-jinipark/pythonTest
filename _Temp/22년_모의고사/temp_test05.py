
# 빙고

MAP = [
    [17,6,9,7,20],
    [13,2,10,3,5],
    [15,18,8,12,14],
    [23,19,4,24,25],
    [22,1,21,11,16]
]

N = [23,3,21,18,8,6,24,13,12,10,9,2,5,15,22,4,11,1,7,20,19,16,17,25,14]


def makeDAT():
    dat = [0] * 30
    for x in range(5):
        for y in range(5):
            num = MAP[x][y]
            dat[num] = (x, y)
    return dat

def getSeroBingoCnt(arr):
    cnt = 0
    for y in range(5):
        flag = 0
        for x in range(5):
            if arr[x][y] == 0 :
                flag = 1
                break

        if flag == 0:
            cnt += 1
    return cnt

def getGaroBingoCnt(arr):
    cnt = 0
    for x in range(5):
        flag = 0
        for y in range(5):
            if arr[x][y] == 0 :
                flag = 1
                break

        if flag == 0:
            cnt += 1
    return cnt

def getDeaBingoCnt(arr):
    cnt = 0
    flag = 0
    for i in range(5):
        if arr[i][i] == 0 :
            flag = 1
            break
    if flag == 0 : cnt += 1

    flag = 0
    for i in range(5):
        if arr[i][4-i] == 0:
            flag = 1
            break
    if flag == 0 : cnt += 1

    return cnt

def isBingo(arr):
    a = getSeroBingoCnt(arr)
    b = getGaroBingoCnt(arr)
    c = getDeaBingoCnt(arr)
    print(a, b, c)

    if a + b + c >= 3 : return True
    return False

def solution():

    # dat 만든다
    dat = makeDAT()
    print(dat)

    # 색칠
    arr = [[0]* 5 for _ in range(5)]

    for tar in N:
        tarX, tarY = dat[tar]
        arr[tarX][tarY] = 1   # 체크
        print('>', tar)
        if isBingo(arr):
            print('tar:', tar)
            return tar

    return 0

# 마지막 수 출력
print(solution())

print('==============================')

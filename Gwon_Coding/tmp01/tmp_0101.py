

MAP = [[17, 6, 9, 7, 20], [13, 2, 10, 3, 5], [15, 18, 8, 12, 14], [23, 19, 4, 24, 25], [22, 1, 21, 11, 16]]
N = [23, 3, 21, 18, 8, 6, 24, 13, 12, 10, 9, 2, 5, 15, 22, 4, 11, 1, 7, 20, 19, 16, 17, 25, 14]

print(MAP)

# 방문기록 처럼 체킹이 필요
bingo = [[0]*5 for _ in range(5)]
print(bingo)

def findXY(no) :
    for i in range(len(MAP)):
        for j in range(len(MAP[0])) :
            if MAP[i][j]  == no :
                return i, j

def chkXY(x, y) :
    #가로 확인
    for i in range(len(bingo)):
        #print(bingo[x][i])
        if bingo[x][i] == 0 :
            return False
    for j in range(len(bingo)):
        #print(bingo[j][y])
        if bingo[j][y] == 0 :
            return False
    return True

def chkXX(x, y) :
    # 대각선
    if x == y :
        for i in range(len(bingo)):
            if bingo[i][i] == 0 :
                return False
        return True
    else :
        return False

def chkYY(x, y) :
    # 역대각선
    N = len(bingo)

    for i in range(len(bingo)):
        if bingo[i][N-1-i] == 0 :
            return False
    return True

def solution(MAP, N):
    answer = 0

    for i in N :
        #print(i)
        x, y =  findXY(i)
        #print(x, y)
        bingo[x][y] = 1

        # 여기서 빙고 체크하는 함수들
        # 가로 세로
        print(chkXY(x, y))
        # 대각선
        print('>', chkXX(x, y))
        # 역대각선
        print('>>', chkYY(x, y))

        if chkXY(x, y) :
            if chkXX(x, y) or chkYY(x, y):
                answer = i
                break

    print(bingo)

    return answer

a = solution(MAP, N)
print(a)
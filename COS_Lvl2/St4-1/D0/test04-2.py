
#프로그래머스 모의고사
#꽃피우기

# v1 하다보니 for loop 도는 도중에
# 상하좌우를 1 로 바꾸니 이번에 1 로 바꾼 상하좌우를 또 바꾸는 형국이 됨
# 금번 회차 시작전 상태를 찍어 놓고 그것만 돌려야 할 듯

# 다음과 같이 import를 사용할 수 있습니다.
# import math

def make_one(n, garden, posX, posY):
    # 상하좌우 활용
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        newX = posX + dx[i]
        newY = posY + dy[i]
        if 0 <= newX < n and 0 <= newY < n :
            garden[newX][newY] = 1

def chek_all_one(n, garden):
    for i in range(n):
        for j in range(n):
            if garden[i][j] == 0:
                return False
    return True

def print2list(lst):
    for i in range(len(lst)):
        print(lst[i])

def copy2list(n,src, tgt):
    for i in range(n):
        for j in range(n):
            tgt[i][j] = src[i][j]
    return tgt

def solution(garden):
    # 여기에 코드를 작성해주세요.
    answer = 0
    n = len(garden)
    while not chek_all_one(n, garden):
        # 한번씩 돌때 사진찍 듯이 찍어 놈
        tmp_copy = [[0 for _ in range(n)] for _ in range(n)]
        tmp_copy = copy2list(n, garden, tmp_copy)
        print(tmp_copy)

        posX = 0;
        posY = 0;
        # 1 의 위치 파악 (여기서 copy 해놓은 tmp_copy list 로 파악)
        for i in range(n):
            for j in range(n):
                if tmp_copy[i][j] == 1:  # ***
                    posX = i;
                    posY = j;
                    # 상하좌우를 1로 만드는 함수
                    make_one(n, garden, posX, posY)
                    print(posX, posY)
        print2list(garden)

        answer += 1

    return answer


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
garden1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
ret1 = solution(garden1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

garden2 = [[1, 1], [1, 1]]
ret2 = solution(garden2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")
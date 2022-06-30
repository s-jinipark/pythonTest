
#프로그래머스 모의고사
#꽃피우기

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

def print2list(lst):
    for i in range(len(lst)):
        print(lst[i])

def solution(garden):
    # 여기에 코드를 작성해주세요.
    answer = 0
    # 상하좌우 활용
    #dx = [-1, 1, 0, 0]
    #dy = [0, 0, -1, 1]

    n = len(garden)

    posX = 0;
    posY = 0;
    # 1 의 위치 파악
    for i in range(n):
        for j in range(n):
            if garden[i][j] == 1:
                posX = i;
                posY = j;
                # 상하좌우를 1로 만드는 함수
                make_one(n, garden, posX, posY)
                print(posX, posY)
                print2list(garden)
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
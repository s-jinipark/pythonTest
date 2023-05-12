# 다음과 같이 import를 사용할 수 있습니다.
# import math
def exist0(garden):
    rtn = False
    for g in garden:
        if 0 in g :
            rtn = True
            break
    return rtn

def start_point(garden):
    s = [-1,-1]
    for i in range(len(garden)):
        for j in range(len(garden[i])):
            print(i, j, garden[i][j])
            if garden[i][j] == 1 :
                s[0] = i
                s[1] = j
                return  s
    return s

def solution(garden):
    # 여기에 코드를 작성해주세요.
    answer = 0

    # if 0 in garden[0] :
    #     print('k')

    # start point
    s = start_point(garden)
    print(s)

    # while exist0(garden):
    #     print('k')


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

#프로그래머스 모의고사
#파트1. 빈 칸 채우기
#Up and down

def solution(K, numbers, up_down):
    left = 1
    right = K
    for num, word in zip(numbers, up_down):
        if word == "UP":
            print("UP", left, num)
            left = max(left, num)

        elif word == "DOWN":
            print("DOWN", right, num)
            right = min(right, num)

        elif word == "RIGHT":
            return 1
    return right-left-1


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
K1 = 10
numbers1 = [4, 9, 6]
up_down1 = ["UP", "DOWN", "UP"]
ret1 = solution(K1, numbers1, up_down1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

K2 = 10
numbers2 = [2, 1, 6]
up_down2 = ["UP", "UP", "DOWN"]
ret2 = solution(K2, numbers2, up_down2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")

K3 = 100
numbers3 = [97, 98]
up_down3 = ["UP", "RIGHT"]
ret3 = solution(K3, numbers3, up_down3)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret3, "입니다.")

'''
UP 1 2
UP 2 1
DOWN 10 6
solution 함수의 반환 값은 3 입니다.

이렇게 2 부르고 UP 이면 2 이상을 불러야 되는데,
다시 1 을 불러서 문제가 발생
'''
def solution(K, numbers, up_down):
    left = 1
    right = K
    for num, word in zip(numbers, up_down):
        if word == "UP":
            #left = num + 1   # 1st
            #left = max(num, left) +1   # 2nd
            left = num+1 if num >= left else left   # 3rd
        elif word == "DOWN":
            #right = num - 1   # 1st
            #right = min(num, right)-1  # 2nd
            right = num-1 if num <= right else right   # 3rd
        elif word == "RIGHT":
            return 1
        print(num, '>', left, right)
    #return right - left   # 1st : 2, 3, 1 이 나와야 하는데 1,3,1 이 나옴
    return right - left + 1    # 3rd


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

import random
import os

numbers = []  # 3자리 저장
number = str(random.randint(0,9)) # 최초 수행 됨
# random.randint( .. 는 두 번 나올 수 밖에 없네.. , for 문 내에도 있음

for i in range(3) :
    while number in numbers :  # 숫자가 있는 동안.. 즉 없는게 나올 때 까지 돈다는 의미
        number = str(random.randint(0, 9))
    numbers.append(number)
print(numbers)

# 인덱싱 처리 하기 위해서 문자열로 받는다
#user_input = str(input("3 자리 숫자를 입력하세요 > "))
#print(user_input)
# => while 문 안으로 이동

os.system("cls")
print("*" * 40)
print("     야구 게임을 시작합니다.")
print("*" * 40)

count_strike = 0
count_ball = 0
count_try = 0

while count_strike < 3 :  # 스트라이크 3개면 종료
    count_strike = 0   # 여기서 다시 초기화
    count_ball = 0
    user_input = str(input("3 자리 숫자를 입력하세요 > "))
    if len(user_input) == 3 :
        for i in range(0, 3) :  # 사용자 입력과
            for j in range(0, 3) :  # random 값 비교
                if user_input[i] == numbers[j] and i == j :
                    count_strike += 1  # i, j 가 같다는 얘기는 자리(순서)도 같다
                elif user_input[i] == numbers[j] and i != j :
                    count_ball += 1
        if count_strike == 0 and count_ball == 0 :
            print(" 3 아웃 !! ")
        else :
            output = ""
            if count_strike > 0 :
                output += " {} 스트라이크 ".format(count_strike)
            if count_ball > 0 :
                output += " {} 볼 ".format(count_ball)
            print(output)
        count_try += 1
print("게임 성공 !! (누적 {} 회)".format(count_try))
import random
import os

numbers = []
number = str(random.randint(0, 9))

for i in range(3) :   # 3번 수행
    while number in numbers:
        number = str(random.randint(0, 9))
    numbers.append(number) # numbers 에 없으면 추가해준다

os.system("cls")

print("*" * 60)
print("야구 게임을 시작합니다. !!!")
print("*" * 60)

count_strike = 0
count_ball = 0
# [2]
count_try = 0

while count_strike < 3 :
    num = str(input("숫자 3자리를 입력하세요> "))

    if len(num) == 3:
        count_strike = 0
        count_ball = 0
        for i in range(0, 3):
            for j in range(0, 3):
                if num[i] == numbers[j] and i == j :  #값이 같고 위치도 같은 경우
                    count_strike += 1
                if num[i] == numbers[j] and i != j : #값은 같으나 위치 다른 경우
                    count_ball += 1
        if count_strike == 0 and count_ball == 0 :
            print(" 3 아웃 !!")
        else :
            output = ""
            if count_strike > 0 :
                output += "{} 스트라이크".format(count_strike)
            if count_ball > 0 :
                output += " {} 볼".format(count_ball)

            print(output.strip())  # 볼만 나왔을 경우 고려
        count_try += 1

#print(numbers)  
#print("게임 성공")
print("게임 성공, {}회 시도".format(str(count_try)))

import os
import random

'''
  1. 입력받은 숫자와 random 생성과 비교
  2. 한번만에 끝나니 10번의 기회를 부여
  3. 입력 값 첵
'''
'''
ran_num = random.randint(1,100)
user_input = input("숫자를 입력하세요 (1~100) > ")

print(">>" + user_input)

if (ran_num == user_input) :
    print("정답.")
else :
    print("아닙니다.")
'''
# 3
def input_check(msg, casting=int) :
    while True :
        try:
            user_input = casting(input("몇 일까요?? "))
            return user_input
        except:
            continue
# 2
chance = 10
count = 0
number = random.randint(1,99)
os.system("cls")
print("1 부터 99 까지의 숫자를 10번 안에 맞춰 보세요. ")
while count < chance :
    count += 1
    #user_input = int(input("숫자를 입력하세요 (1~99) > "))
    # 3
    user_input = input_check("몇 일까요 ?? ?? ")
    if number == user_input:
        #print("정답.")
        break
    elif user_input < number :
        print("{} 보다 큰 숫자 입니다.".format(user_input))
    elif user_input > number :
        print("{} 보다 작은 숫자 입니다.".format(user_input))

if user_input == number :
    print(" 성공 ! {} 이 맞습니다.".format(number))
else :
    print(" 실패 ! 정답은 {} 입니다.".format(number))


import random

select_num = random.randint(1, 99)
chance = 10  # 10 회 수행
count = 0
#print(select_num)

while (count < chance):
    count += 1

    input_num = int(input("숫자를 입력하세요."))

    if (select_num == input_num):
        #print("정답")
        break
    elif (select_num > input_num):
        print("숫자가 {} 보다 큽니다".format(input_num))
    elif (select_num < input_num):
        print("숫자가 {} 보다 적습니다".format(input_num))

if (select_num == input_num):
    print("정답")
else :
    print("실패 - 다음 기회에..")


#if name == "홍길동":
#    # 들여쓰기


# 조건문
# 현재 시간이 12시면 점심을 먹고 아니면 일을 한다

time = 12

if time == 12 :
    print('점심 먹으러감')
else:
   print('일하는 중..')


# 현재 시간이 12부터 1시 이전이면 점심을 먹고 아니면 일을 한다

if time >= 12 and time < 1:  # if 12 <= time < 1: (이렇게 써도 됨)
    print('점심 먹으러감')
else:
   print('일하는 중..')


# 현재 시간이 12부터 1시 이전이면 점심을 먹고 
# 3시 부터 4시 까지는 일을 하고 아니면 일을 한다

if 12 <= time  < 13: 
    print('점심 먹으러감')
elif 3 <= time <= 4: 
    print('휴식시간')
else:
   print('일하는 중..')


name = "abcdef"
if "a" in name:
    print("있음")
else:
    print("없음")


name = ["홍길동", "가가멜", "가제트"]
if "가제트" not in name:
    print("없음")
else:
    print("있음")


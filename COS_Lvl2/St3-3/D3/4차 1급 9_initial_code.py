# 다음과 같이 import를 사용할 수 있습니다.
# import math

def solution(hour, minute):
    answer = ''
    # 1도 생각 안나 솔루션 봄
    hour_pos = float(hour) * 30.0 + float(minute) * 0.5
    minute_pos = float(minute) * 6.0
    #-> 각 시간은 360 / 12 = 30 이므로 30도 씩
    #   30도 를 분에 따라 나누면 30/60분 = 0.5
    #-> 각 분은 360 / 60 = 0.6
    answer = abs(hour_pos - minute_pos)

    if answer > float(360) - answer :
        answer = float(360) - answer

    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
hour = 3
minute = 0
ret = solution(hour, minute)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")


hour = 2
minute = 15
ret = solution(hour, minute)
print("solution 함수의 반환 값은 ", ret, " 입니다.")

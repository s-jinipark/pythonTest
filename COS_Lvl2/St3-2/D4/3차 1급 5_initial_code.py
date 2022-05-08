# 다음과 같이 import를 사용할 수 있습니다.
# import math

def solution(phrases, second):
    # 여기에 코드를 작성해주세요.
    answer = ''
    p_len = len(phrases)
    print(p_len)
    # 14 까지의 구간과
    # 28 까지의 구간으로 나누어서 접근
    #print(18%14)
    #print(29//14) # 짝수가 나오면 지나가기 전.. , 홀수가 나오면 지나간 뒤
    chk1 = second % p_len
    chk2 = second // p_len
    print(chk1)
    print(chk2)
    # padding 을 만든다
    tmp = ''

    if chk2 % 2 == 0 : # 짝수면 지나가기 전
        # 앞에서 부터 슬라이스
        #print(phrases[:chk1])
        for i in range(p_len - chk1):
            tmp += '_'
        # 앞에다 padding 시켜야
        tmp += phrases[:chk1]
    else :
        # 뒤에서 부터 슬라이스
        #print(phrases[chk1:])
        for i in range(chk1):
            tmp += '_'
        # 뒤에 padding 시켜야
        tmp = phrases[chk1:] + tmp
    print(tmp)
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
phrases = "happy-birthday"
second = 29
ret = solution(phrases, second)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")

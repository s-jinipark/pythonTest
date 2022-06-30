#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(number, target):
    #여기에 코드를 작성해주세요.
    answer = 0
    '''
    연산1.  1을 더합니다
    연산2.  1을 뺍니다
    연산3.  2를 곱합니다
    '''
    cnt1 = 0  # target 보다 적은 경우
    cnt2 = 0  # target 보다 큰 경우

    # 곱하기를 먼저 했을 때 넘지 않는 경우와 넘는 경우 비교 (하면 될 거 같은데..)
    while True :
        number = number * 2
        stop = False
        if number == target :
            #break
            stop = True
        elif number > target :
            # * 2 해서 넘었을 경우
            # 2가지 값을 비교
            pre_num = number/2
            while True :
                cnt1 += 1
                cnt2 -= 1
                if (pre_num + cnt1) == target :
                    answer += cnt1
                    stop = True
                    break
                if (number + cnt2) == target :
                    answer += abs(cnt2)
                    stop = True
                    break
        answer += 1
        if stop :
            break
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
number1 = 5
target1 = 9
ret1 = solution(number1, target1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

number2 = 3
target2 = 11
ret2 = solution(number2, target2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")
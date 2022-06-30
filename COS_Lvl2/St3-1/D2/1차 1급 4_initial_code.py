#You may use import as below.
#import math

def solution(num):
    # Write code here.
    answer = 0
    num = num +1
    print(num)

    # 올림이 없으니 0 -> 1 로 바꾸면 될 듯
    tmp = str(num)
    tmp2 = ''
    for c in tmp :
        #print(c)
        if c == '0':
            tmp2 += '1'
        else :
            tmp2 += c
    answer = int(tmp2)
    return answer


def solution2(num):
    answer = 0
    num += 1
    digit = 1

    while num // digit % 10 == 0:
        print(num, digit, num // digit % 10)
        num += digit
        digit *= 10
    answer = num
    return answer


#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
num = 9949999
ret = solution(num)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("Solution: return value of the function is", ret, ".")

num = 9949999
ret = solution2(num)
print("Solution: return value of the function is", ret, ".")
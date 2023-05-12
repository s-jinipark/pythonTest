def solution(num):
    num += 1
    digit = 1
    while num // digit % 10 == 0:
        print(num, digit, num // digit % 10)
        num += digit
        digit *= 10
    return num

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
num = 9949999
ret = solution(num)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("Solution: return value of the function is", ret, ".")
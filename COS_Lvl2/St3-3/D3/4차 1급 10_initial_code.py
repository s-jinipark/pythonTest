#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(a, b):
    # 여기에 코드를 작성해주세요.
    answer = 0
    for i in range(a, b+1):
        #print(i)
        for j in range(2, i):
            if i % j == 0 :
                break
        else :
            answer += 1
            print(i, i*i, i*i*i)
            #print(i, i^2, i^3)
    return answer
    #=> 잘 안됨

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
a =  6
b =  30
ret = solution(a, b)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
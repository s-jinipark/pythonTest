#다음과 같이 import를 사용할 수 있습니다.
#import math

def func_a(bishops) :
    n = len(bishops)
    print(n)
    rtn = []
    for b in bishops:
        x = b[1]
        y = b[0]
        print(x, y, ord(y), ord('A'))
        x2 = 8 - int(x)
        y2 = int(ord(y)) - 65
        rtn.append((x2, y2))
    return rtn

def solution(bishops):
    #여기에 코드를 작성해주세요.
    answer = 0

    # 좌표 헷갈려서 난 일단 변환
    rtn_a = func_a(bishops)
    print(rtn_a)




    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
bishops1 = ["D5"]
ret1 = solution(bishops1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

bishops2 = ["D5", "E8", "G2"]
ret2 = solution(bishops2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")
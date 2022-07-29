#다음과 같이 import를 사용할 수 있습니다.
#import math

def func_a(bishops) :
    n = len(bishops)
    #print(n)
    rtn = []
    for b in bishops:
        x = b[1]
        y = b[0]
        #print(x, y, ord(y), ord('A'))
        x2 = 8 - int(x)
        y2 = int(ord(y)) - 65
        rtn.append((x2, y2))
    return rtn

def func_b(rtn_a) :
    #print(rtn_a)
    pos_x = [-1, -1, 1, 1]  # 10시, 2시, 5시, 7시
    pos_y = [-1, 1, 1, -1]
    rtn = []
    for r in rtn_a:
        #print(r[0], r[1])
        tmp_x = r[0]
        tmp_y = r[1]
        # 현위치도 포함시켜야 할 듯
        rtn.append((tmp_x, tmp_y))
        for n in range(1,8): #  8 * 8  이니까 일단
            for p in range(4) :  #  4 방향
                tmp_x += pos_x[p] * n
                tmp_y += pos_y[p] * n
                if 0<= tmp_x < 8  and 0<= tmp_y < 8 :
                    rtn.append((tmp_x, tmp_y))
        #print(rtn)
    return rtn

def solution(bishops):
    #여기에 코드를 작성해주세요.
    answer = 0

    # 좌표 헷갈려서 난 일단 변환
    rtn_a = func_a(bishops)
    print(rtn_a)  # 비숍이 있는 곳

    rtn_b = func_b(rtn_a)
    print(rtn_b)

    # 1 로 셋팅
    tmp_bishops = [[0]*8]*8
    print(tmp_bishops)
    for r in rtn_b :
        print(r[0],r[1])
        tmp_bishops[r[0]][r[1]] = 1
    print(tmp_bishops)

    cnt = 0
    # 0 인 갯수 세기
    for i in range(8):
        for j in range(8):
            if tmp_bishops[i][j] == 0 :
                cnt +=1
    answer = cnt
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
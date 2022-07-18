#You may use import as below.
#import math

def solution(pos):
    # Write code here.
    answer = 0

    # 기존 이차원 배열 형식이 아니라
    # A7 ?? 변형된 형식인데..
    print(ord('A'))  # 65
    print(ord('H'))  # 72
    # 행은 8 - 넘어 온 숫자 = index 가 되고
    # 열은 ord(알파벳) - 65 해주면 됨

    # 변환
    row = pos[1]
    col = pos[0]
    print(row, col)
    row2 = 8 - int(row)
    col2 = ord(col) - 65
    print(row2, col2)

    # 상하 좌우 하는거 ...
    pos_x = [-2, 2, 0, 0]
    pos_y = [0, 0, -2, 2]
    cnt = 0

    for i in range(4) : #4 방향
        if 0 <= row2 + pos_x[i] < 8 :
            if 0 <= col2 + pos_y[i] < 8 :
                #cnt += 1
                # 상하 2 칸 이동 했으면 -> 좌우 1 칸
                # 좌우 2 칸 이동 했으면 -> 상하 1 칸
                if i < 2 : # 상하 인 경우니 좌우 점검
                    # 여기까지 잘 왔고, 좌우 만 봐주면 됨
                    if 0 <= col2 + pos_y[i] - 1 < 8 :
                        cnt += 1
                    if 0 <= col2 + pos_y[i] + 1 < 8 :
                        cnt += 1
                else :
                    if 0 <= row2 + pos_x[i] - 1 < 8 :
                        cnt += 1
                    if 0 <= row2 + pos_x[i] + 1 < 8 :
                        cnt += 1
    print(cnt)

    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
pos = "A7"
ret = solution(pos)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("Solution: return value of the function is", ret, ".")
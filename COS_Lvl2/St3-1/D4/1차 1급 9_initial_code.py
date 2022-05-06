def func(record):
    if record == 0:
        return 1
    elif record == 1:
        return 2
    return 0

def solution(recordA, recordB):
    cnt = 0
    for i in range(len(recordA)):
        if recordA[i] == recordB[i]:
            continue
        elif recordA[i] == func(recordB[i]):
            cnt = cnt + 3
        else:
            #cnt = cnt - 1
            cnt = max(0, cnt - 1)   # 몰랐음
    return cnt

#원소는 0, 1, 2 중 하나이고 순서대로 가위 , 바위 , 보를 의미합니다

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution 함수만 수정하세요.
recordA = [2,0,0,0,0,0,1,1,0,0]
recordB = [0,0,0,0,2,2,0,2,2,2]
ret = solution(recordA, recordB)


#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("Solution: return value of the function is", ret, ".")
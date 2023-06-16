

def solution(n, connect):
    answer = 0

    connect.sort()
    print(connect)

    for c in connect:
        tmp = 0
        if c[0]> c[1]:
            tmp = c[0]
            c[0] = c[1]
            c[1] = tmp
    print(connect)

    prev = 1 # 영희의 컴퓨터
    cnt = 1
    for i in range(len(connect)):
        if prev == connect[i][0]:
            cnt += 1
            prev = connect[i][1]
    print(cnt)
    return answer


n = 5   # 컴퓨터의 수
connect = [[1,2],[3,2],[4,5]]
solution(n, connect)

n = 5
connect = [[2,3],[4,3],[3,5]]
solution(n, connect)

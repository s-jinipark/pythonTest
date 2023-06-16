

def solution(n, connect):
    answer = 0

    temp = [[0]* (n+1) for _ in range(n+1)]

    print(temp)

    for c in connect:
        temp[c[0]][c[1]] = 1
        temp[c[1]][c[0]] = 1
    #print(connect)
    print(temp)

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

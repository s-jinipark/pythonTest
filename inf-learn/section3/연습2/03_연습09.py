
##### 봉우리
def solution():
    answer = 0
    # 테두리를 두르자
    tmp = [[0] * (N+2) for _ in range(N+2)]
    #print(연습)
    for i in range(N):
        for j in range(N):
            tmp[i+1][j+1] = inp[i][j]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            #print(i, j)
            for k in range(4):
                if tmp[i][j] < tmp[i+dx[k]][j+dy[k]] :
                    break
            else:
                print( tmp[i][j] )
                cnt += 1

    print(cnt, tmp)
    return answer

N = 5
inp = [
    [5, 3, 7, 2, 3],
    [3, 7, 1, 6, 1],
    [7, 2, 5, 3, 4],
    [4, 3, 6, 4, 1],
    [8, 7, 3, 5, 2]
]
re = solution()
print(re)
#=>
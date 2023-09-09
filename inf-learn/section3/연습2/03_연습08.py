
##### 곳감(모래시계)
def solution():
    answer = 0
    '''
    문제를 2단계로 내네..
    '''
    for c in cmd:
        print(c)
        print(inp[c[0]-1])  # 0 부터 시작하므로, -1 을 해줘야 ...
        tmp1 = inp[c[0]-1]
        tmp2 = [0]* N
        for i in range(len(tmp1)):
            if c[1] == 0:
                tmp = i-c[2]
                if tmp < 0 :
                    tmp = N+tmp
            else :
                tmp = i+c[2]
                if tmp >= N:
                    tmp = tmp -N
            tmp2[tmp] = tmp1[i]
            print(i, tmp)
        inp[c[0]-1] = tmp2
    print(inp)

    '''
    여기는 아까 했던
    '''
    s = 0
    e = 4
    tot = 0
    for i in range(N):
        for j in range(s, e+1):
            print(i,j)
            tot += inp[i][j]
        if i < N//2:
            s+=1
            e-=1
        else:
            s-=1
            e+=1
        print('-----')
    print('tot', tot)
    return answer

N = 5
inp = [
    [10, 13, 10, 12, 15],  # 주의! 여기서부터 1행이라는 ...
    [12, 39, 30, 23, 11],
    [11, 25, 50, 53, 15],
    [19, 27, 29, 37, 27],
    [19, 13, 30, 13, 19]
]
M = 3  # 회전명령의 개수
cmd = [
    [2, 0, 3], # 2 번째 행을 왼쪽으로 3만큼 회전
    [5, 1, 2], # (가운데 1이면 오른쪽) 즉 5번째 행을 오른쪽으로 2만큰 회전
    [3, 1, 4]
]
re = solution()
print(re)
#=> 362
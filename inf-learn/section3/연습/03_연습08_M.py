
##### 곳감(모래시계)
def solution():
    answer = 0
    for c in cmd:
        src = inp[c[0]-1]
        tgt = [0] * N

        print(c)
        for i in range(N):
            if c[1] == 0 : # 왼쪽부터
                if i-c[2] < 0:
                    print(i, N+(i-c[2] ))
                    tgt[N+(i-c[2] )] = src[i]
                else :
                    print(i, i-c[2])
                    tgt[ i-c[2] ] = src[i]
            else:
                if i+c[2] > N-1:
                    print(i, i+c[2]-N)
                    tgt[ i+c[2]-N ] = src[i]
                else :
                    print(i, i+c[2])
                    tgt[ i+c[2] ] = src[i]
        print(src, tgt)
        # src 변경
        #src = tgt  # 이거 안됨
        print(src)
        for i in range(N):
            inp[c[0]-1][i] = tgt[i]
    print(inp)
    sum = 0
    # 그 다음 모래시계
    for i in range(N//2+1):
        print(i)
        for j in range(i, N-i):
            print(j, end= ' ')
            sum += inp[i][j]
        print()
    print('-----')
    #반대
    offs = 0
    for i in range(N-1, N//2, -1):
        print(i)
        for j in range(offs, N-offs):
            print(j, end= ' ')
            sum += inp[i][j]
        print()
        offs += 1
    answer = sum
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
    [5, 1, 2], # (가운데 1이면 오른쪽)
    [3, 1, 4]
]
re = solution()
print(re)
#=> 362
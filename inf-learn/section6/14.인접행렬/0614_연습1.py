
# self
def solution(N):
    answer = 0

    print(rtn)
    for i in  inp:
        x, y, val = i
        #print(x,y)
        rtn[x][y] = val

    #print(rtn)
    for j in range(1, N+1):
        for k in range(1, N+1):
            print(rtn[j][k], end=' ')
        print()
    return answer

# 인접 행렬을 출력
# 정점의 수 N(2<=N<=20)와 간선의 수 M가 주어진다.
N = 6
M = 9
inp = [
    [1, 2, 7],
    [1, 3, 4],
    [2, 1, 2],
    [2, 3, 5],
    [2, 5, 5],
    [3, 4, 5],
    [4, 2, 2],
    [4, 5, 5],
    [6, 4, 5]
]
#rtn = ''
rtn = [[0] * (N+1) for _ in range(N+1)]
#=> 하나 여유로 잡아서, 숫자를 그대로 index 로

re = solution(N)
print('re :', re)



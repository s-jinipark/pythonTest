
# BFS , 이 경우 최단 거리는 아님..
from collections import deque

def solution():
    answer = 0
    qu = deque()
    #start 는 중앙
    start = N//2
    print(start)
    qu.append( (start,start) )
    sum = inp[start][start]
    visted[start][start] = 1
    dx = [-1,1,0,0]  # 상하 [행렬 스타일이니까 x 가 상하]
    dy = [0,0,-1,1]  # 좌우

    # L= 0
    # while True:
    #     if L == N//2:
    #         break
    #     size = len(qu)  # 이거 를 왜 하는지? 없으면
    #     for i in range(size):
    #         now = qu.popleft()
    #         print('now:', now)
    #         for j in range(4):
    #             next_x = now[0] + dx[j]
    #             next_y = now[1] + dy[j]
    #             #print('>', next_x, next_y)
    #             if visted[next_x][next_y] == 0 :
    #                 sum += inp[next_x][next_y]
    #                 visted[next_x][next_y] =1
    #                 qu.append((next_x, next_y))
    #     L += 1

    ##### 1st 시도 - 틀림
    L = 0
    while qu:
        if L == N//2:
            break
        now = qu.popleft()
        print('now:', now)
        for i in range(4): # 4방향이니까.
            next_x = now[0] +dx[i]
            next_y = now[0] +dy[i]
            print('>', next_x, next_y)
            if visted[next_x][next_y] == 0:
                qu.append((next_x,next_y))
                visted[next_x][next_y]=1
                sum += inp[next_x][next_y]
        L += 1

    print('sum:', sum)
    return answer


N = 5   # 홀수 [라고 문제에 적어 놈]
inp = [
    [10, 13, 10, 12, 15],
    [12, 39, 30, 23, 11],
    [11, 25, 50, 53, 15],
    [19, 27, 29, 37, 27],
    [19, 13, 30, 13, 19]
]
visted = [[0]*N for _ in range(N)]
print(visted)

re = solution()
print('re :', re)
#=>
print('==============================')

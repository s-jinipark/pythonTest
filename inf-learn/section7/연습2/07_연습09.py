
##### 미로의 최단거리 통로(BFS 활용)
from collections import deque
def solution():
    answer = 0

    '''
    출발점은 (1,1) , 도착점은(7,7)
    여기서는 index 고려 0,0  ->  6,6 으로 
    
    최단.. 나오면 BFS
    1 은 벽이고, 0 은 도로
    '''
    qu = deque()
    qu.append((0,0))  # start
    ch[0][0] = 1  # 엥 여기 1로 해야 함?

    while qu :
        cur = qu.popleft()
        if cur[0]== 6 and cur[1] == 6:
            print(ch)
            break
        for i in range(4):
            n_x = cur[0] + dx[i]
            n_y = cur[1] + dy[i]
            # 범위체크, 방문체크, 벽인지 체크
            if 0<= n_x < N and 0<= n_y < N :
                if inp[n_x][n_y] == 0 and ch[n_x][n_y] == 0:  # 벽이 아니어야.. 방문도 안했어야..
                    ch[n_x][n_y] = ch[cur[0]][cur[1]] +1
                    qu.append((n_x, n_y))
    #print(ch)
    print('>', ch[6][6]-1)  # 다시 -1 해줬는데, 이 방법 밖에 없나?
    # 0 부터 시작하면, 방문했다는 표시가 안되서 1 로 해는데,
    # 해설에서는 inp 를 1 로 만들어 버림, ch 는 순수 횟수로만 사용(그래서 0 으로 시작)

    return answer

N = 7

inp = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [1, 1, 0, 1, 0, 1, 1],
    [1, 1, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 0]
]
#방문기록
ch = [[0]* N for _ in range(N)]

dx = [ -1, 0, 1, 0]  # 시계 방향으로
dy = [0, 1, 0, -1]

re = solution()
print(re)
#=>
print('====================')

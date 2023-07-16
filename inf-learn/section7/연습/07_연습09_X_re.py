
##### 미로의 최단거리 통로(BFS 활용)
from collections import deque
def solution():
    answer = 0

    '''
    출발점은 (1,1) , 도착점은(7,7)
    여기서는 index 고려 0,0  ->  6,6 으로 
    '''

    qu = deque()
    qu.append((0,0))
    #ch[0][0] = 1  # 방문 기록 X  , [2] 누적 값으로 변경
    # [2] 방문기록을 하니까 마지막에 +1 된 수가 나와서.. 흠
    # 강의 보니 벽으로 만들어 버린다...
    # 근데 어떤 건 주어진 배열을 조작하고,  어떤건 방문기록을 남기고... 헷갈린다..
    inp[0][0] = 1  # 벽으로 만들어 버린다.
    cnt =0
    while qu :
        now = qu.popleft()
        print(now)
        # cnt += 1
        # if now[0] == N-1 and now[1]==N-1 :
        #     print( '>', ch[now[0]][now[1]] )
        #     break
        # [2] => 마지막에 해줌

        #print(now)
        # 4가지 방향
        for i in range(4):
            #next = (now[0]+ dx[i], now[1] + dy[i])
            # [2] 이거보다 x, y 가 간편한 듯
            x = now[0]+ dx[i]
            y = now[1] + dy[i]
            # if 0<= next[0] < N and 0<= next[1] < N :
            #     if inp[next[0]][next[1]] == 0 and ch[next[0]][next[1]] == 0 :
            #         # 벽이 아니면서, 방문이력도 없는. 곳
            #         #ch[next[0]][next[1]] = 1
            #         ch[next[0]][next[1]] = ch[now[0]][now[1]] + 1
            #         # [2] 여기를 그냥 1 넣을 게 아니라.. (이전 + 1) 해서 ...
            #         qu.append((next[0], next[1]))
            #         #print(next)
            if 0<= x < N and 0<= y <N and inp[x][y] == 0:
                inp[x][y] = 1   # 벽으로 만들어 버려
                ch[x][y] = ch[now[0]][now[1]] +1
                qu.append((x,y))   # x, y 에 할당하고 쓰는게 훨 편하고, 오류 없을 듯

    # 마지막값을 출력하면 되는데,
    # 만약 0 이면 못 왔다는 얘기
    if ch[6][6] == 0 :
        print(-1)
    else :
        print(ch[6][6])

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


##### 미로의 최단거리 통로(BFS 활용)
from collections import deque
def solution():
    answer = 0

    '''
    출발점은 (1,1) , 도착점은(7,7)
    '''
    for i in inp:
        i.insert(0,0)
    inp.insert(0, [0] * (7+1))
    #print(inp)
    for j in inp:
        print(j)
    # 위쪽하고, 왼쪽에 0 을 넣어주어
    # (1,1) 출발, (7,7) 도착이 가능하도록 ....

    qu = deque()
    qu.append((1,1))
    ch[1][1] = 1  # 방문

    cnt =0
    while qu :
        now = qu.popleft()
        print(now)
        cnt += 1
        if now[0] == 7 and now[1]==7:
            break
        #print(now)
        # 4가지 방향
        for i in range(4):
            next = (now[0]+ dx[i], now[1] + dy[i])
            if 0< next[0] <=7 and 0< next[1] <=7 :
                if inp[next[0]][next[1]] == 0 and ch[next[0]][next[1]] == 0 :
                    # 벽이 아니면서, 방문이력도 없는. 곳
                    ch[next[0]][next[1]] = 1
                    qu.append((next[0], next[1]))
                    #print(next)
    print('cnt', cnt)
#N = 5

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
ch = [[0]*(7+1) for _ in range(7+1)]

dx = [ -1, 0, 1, 0]  # 시계 방향으로
dy = [0, 1, 0, -1]

re = solution()
print(re)
#=>
print('====================')

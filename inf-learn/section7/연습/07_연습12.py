
##### 단지 번호 붙이기(DFS, BFS)

from collections import deque

def findFirst1() :
    for i in range(N):
        for j in range(N):
            if inp[i][j] == 1:
                return (i, j)
    return(-1, -1)

def solution():
    answer = 0

    '''
    일단 난 BFS 로
     
    ch 만들어서 방문체크 및 단지번호 기록

    '''
    cnt = 1
    tmp = []
    while True:

        fst = findFirst1()
        print(fst)
        if fst[0] == -1:
            break

        qu = deque()

        ch[fst[0]][fst[1]] = cnt
        inp[fst[0]][fst[1]] = 0  # 0 으로 셋팅
        qu.append((fst[0], fst[1]))
        kak_cnt = 0
        while qu :
            now = qu.popleft()
            x = now[0]
            y = now[1]
            kak_cnt += 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < N and ch[nx][ny] == 0 and inp[nx][ny] == 1:
                    inp[nx][ny] = 0
                    ch[nx][ny] = cnt
                    qu.append((nx, ny))
        tmp.append(kak_cnt)
        print('cnt' , cnt)
        answer = cnt   # 여기서 넣어 놔야 나중에 출력 시
        cnt += 1

        for c in ch:
            print(c)
    print(tmp)
    return answer

N = 7

inp = [
    [0, 1, 1, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 1, 1],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 0, 0, 0]
]
#방문기록
ch = [[0]*N for _ in range(N)]

dx = [ -1, 0, 1, 0]  # 시계 방향으로
dy = [0, 1, 0, -1]

cnt = 0

re = solution()
print(re)
#=>
print('====================')

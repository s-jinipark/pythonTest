
##### 섬나라 아일랜드(BFS 활용)

from collections import deque
def findFirst1():
    for i in range(N):
        for j in range(N):
            if inp[i][j] == 1 :
                return (i, j)
    return(-1,-1) # 여기까지 오면 없다는 말

def solution():
    answer = 0

    '''
    기존 "단지 번호 붙이기" 와 유사
    
    아일랜드는 인제 BFS 로 하자!
     
    ch 만들어서 방문체크 및 번호 기록

    [2] 문제 잘 봐야 될 듯 
        이건 대각선 까지 연결로 봄 
    '''
    cnt = 1
    while True:
        fst = findFirst1()
        print(fst)
        if fst[0] == -1 :
            break

        qu = deque()

        ch[fst[0]][fst[1]] = cnt  # 방문기록
        inp[fst[0]][fst[1]] = 0   # 중요.. 이거 자꾸 빠트림.. (하나 할 땐 괜찮은데...)
        qu.append((fst[0], fst[1]))

        while qu:
            now = qu.popleft()
            x = now[0]
            y = now[1]
            for i in range(8):  # (4):  # [2] 대각선 까지
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<= nx < N and 0<= ny < N and ch[nx][ny] == 0  and inp[nx][ny] == 1 : # 방문 안했고 섬이냐.?
                    ch[nx][ny] = cnt  # 1이 아니고
                    inp[nx][ny] = 0   # 바다로 만들어.. ㅋ
                    qu.append((nx, ny))

        answer = cnt
        cnt += 1
        # 확인
        for c in ch:
            print(c)

    # 초벌로 이렇게 해놓고....
    # 루핑 돌로록
    # fst = findFirst1()
    # print(fst)
    #
    # qu = deque()
    # cnt = 1
    # ch[fst[0]][fst[1]] = cnt  # 방문기록
    # qu.append((fst[0], fst[1]))
    #
    # while qu:
    #     now = qu.popleft()
    #     x = now[0]
    #     y = now[1]
    #     for i in range(4):
    #         nx = x + dx[i]
    #         ny = y + dy[i]
    #         if 0<= nx < N and 0<= ny < N and ch[nx][ny] == 0  and inp[nx][ny] == 1 : # 방문 안했고 섬이냐.?
    #             ch[nx][ny] = cnt  # 1이 아니고
    #             inp[nx][ny] = 0   # 바다로 만들어.. ㅋ
    #             qu.append((nx, ny))
    #
    # # 확인
    # for c in ch:
    #     print(c)
    return answer

N = 7

inp = [
    [1, 1, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 1],
    [1, 1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 1, 0, 0]
]
#방문기록
ch = [[0]*N for _ in range(N)]

# dx = [ -1, 0, 1, 0]  # 시계 방향으로
# dy = [0, 1, 0, -1]
#[2] 대각선 까지 해줘야
dx = [ -1, -1, 0, 1, 1,  1,  0, -1]  # 시계 방향으로
dy = [  0,  1, 1, 1, 0, -1, -1, -1 ]

cnt = 0

re = solution()
print(re)
#=>
print('====================')

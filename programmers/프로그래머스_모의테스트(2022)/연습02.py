
# 경로 탐색 - DFS
def DFS(L):
    global cnt
    if L == N :
        cnt += 1
        return
    else:
        for i in range(1, N+1) : # 여기도 N
            # 체크하고 (간선이 있고, 방문하지 않음)
            if g[L][i] == 1 and chk[i] == 0:  # [L][i] 가 핵심
                chk[i] =1
                DFS(i)
                chk[i] = 0  # (중요) 0 으로 만들어 줌

def solution(N):
    answer = 0

    print(g)
    # 그래프 셋팅
    for i in  inp:
        x, y = i
        #print(x,y)
        g[x][y] = 1  # 행에서 열로 이동
    print(g)

    chk[1] =1  # [시작점도 어떨때 0이고 1 인지 구분 필요]
    DFS(1)  # 1번 시작

    return answer


# 정점의 수 N 와 간선의 수 M
N = 5   # 정점
M = 9   # 간선
inp = [
    (1, 2),
    (1, 3),
    (1, 4),
    (2, 1),
    (2, 3),
    (2, 5),
    (3, 4),
    (4, 2),
    (4, 5)
]

g = [[0] * (N+1) for _ in range(N+1)]
#=> 하나 여유로 잡아서, 숫자를 그대로 index 로
chk =  [0] * (N+1)  # 이것도 1번부터 쓸거라..
cnt = 0

# 그래프와, chk 두개 있어야...

solution(N)
print(cnt)
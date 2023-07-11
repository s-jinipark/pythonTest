
##### 인접행렬(가중치 방향그래프)

def DFS(v) :  # 노드 번호
    if v == N :  # 종착점
        print('>', ch)
        # 경로 찍으려 했으나, 이렇게 하면 order 를 알 수 없음
        # for i in range(1, N+1):
        #     if ch[i] == 1:
        #         print(i, end=' ')
        # print()
        for x in path:
            print(x, end=' ')
        print()
    else :
        for i in range(1, N+1):   # 1번 부터, 0 아님
            if ch[i] == 0  and g[v][i] == 1:  # v -> i 로 이동
                ch[i] = 1
                path.append(i)
                DFS(i)
                path.pop()
                ch[i] = 0

def solution():
    answer = 0

    for i in  inp:
        a, b = i
        #print(a,b)
        g[a][b] = 1
    print(g)

    ch[1] = 1   # 방문 표시
    path.append(1)
    DFS(1)

    return answer

N = 5   # 정점의 수
M = 9   # 간선의 수

g=[[0]* (N+1)  for _ in range(N+1)]
ch = [0] * (N+1)  # 0 은 안 씀
path = []
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

re = solution()
print(re)
#=>
print('====================')

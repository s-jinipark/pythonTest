
##### 경로 탐색(그래프 DFS)
def DFS(v):
    global  cnt
    if v == N:
        #print(ch)
        for x in path:
            print(x, end=' ')
        print()
        cnt += 1
        return
    else :
        # 5 가지로 뻗는데.. g 에 chk 가 되어 있어야
        for i in range(1, N+1):
            if g[v][i] == 1  and ch[i] == 0:
                # => 선이 있어야 가고, 방문하지 않았어야..
                ch[i] = 1
                path.append(i)
                DFS(i)
                path.pop()
                ch[i] = 0

def solution():
    answer = 0

    # g 에 셋팅
    for i in inp:
        g[i[0]][i[1]] = 1

    # for j in range(1, N+1):
    #     for k in range(1, N+1):
    #         print(g[j][k], end=' ')
    #     print()
    '''
    행 -> 열
    이동이라 생각할 것
    '''
    ch[1] =1        # <= [2] 야! 이게 빠졌어
    path.append(1)  # <= [2] 야! 이게 빠졌어
    DFS(1)   # 1부터 시작
    print('cnt: ', cnt)
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
cnt = 0

re = solution()
print(re)
#=>
print('====================')

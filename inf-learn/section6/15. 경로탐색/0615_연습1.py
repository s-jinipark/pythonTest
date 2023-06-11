
# 풀이 듣고 다시

def DFS(v):
    global  cnt
    if v == N:  # 여기 N 임
        cnt += 1
        return
    else:
        # N 가지로 뻗는다
        for i in range(1, N+1):
            # 체크하고 (간선이 있고, 방문하지 않음)
            if g[v][i] == 1 and chk[i] == 0 :
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

    chk[1] =1  # [시작점도 어떨때 0이고 1 인지 구분 필요]
    path.append(1)  # 1번 정점에서 N번 정점으로 가는 모든 경로의 가지 수
    DFS(1)  # 1번이라 말함

    return answer

# self
# def DFS(v):
#     global  cnt
#     if v == N:
#         cnt += 1
#         print(path)
#         return
#     else:
#         # 갈 수 있는 곳만 가는거지
#         for i in range(1, N+1):
#             if g[v][i] ==1 and chk[i] ==0 :
#                 chk[i] = 1
#                 path.append(i)
#                 DFS(i)   # ** i 임
#                 chk[i] = 0
#                 path.pop()
#
# def solution(N):
#     answer = 0
#
#     print(g)
#     # 그래프 셋팅
#     for i in  inp:
#         x, y = i
#         #print(x,y)
#         g[x][y] = 1  # 행에서 열로 이동
#
#     chk[1] =1  # [시작점도 구분이 필요]
#     path.append(1)
#     DFS(1)
#
#     return answer

# 정점의 수 N(2<=N<=20)와 간선의 수 M가 주어진다
N = 5
M = 9
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
#rtn = ''
g = [[0] * (N+1) for _ in range(N+1)]
#=> 하나 여유로 잡아서, 숫자를 그대로 index 로
chk =  [0] * (N+1)  # 이것도 1번부터 쓸거라..
cnt = 0

#[2]
path = []

re = solution(N)
print('re :', re)

print(cnt)

'''
노드 갯수로 가지를 뻗는다
인접 행렬에 있는지 (확인)
방문했는지 (확인)
'''

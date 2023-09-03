
##### 인접행렬(가중치 방향그래프)

def solution():
    answer = 0
    for i in inp:
        print(i)
        g[i[0]][i[1]] = i[2]

    for j in range(1, N+1):
        for k in range(1, N+1):
            print(g[j][k], end=' ')
        print()

    return answer

N = 6   # 정점의 수
M = 9   # 간선의 수

g=[[0]* (N+1)  for _ in range(N+1)]
ch = [0] * (N+1)  # 0 은 안 씀
path = []
inp = [
    (1, 2, 7),
    (1, 3, 4),
    (2, 1, 2),
    (2, 3, 5),
    (2, 5, 5),
    (3, 4, 5),
    (4, 2, 2),
    (4, 5, 5),
    (6, 4, 5)
]

re = solution()
print(re)
#=>
print('====================')

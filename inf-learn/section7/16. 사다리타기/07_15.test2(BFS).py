
# DFS

def solution():
    answer = 0

    return answer

M = 6  # 가로 칸수
N = 4  # 세로 칸수
inp = [
    [0, 0, -1, 0, 0, 0],
    [0, 0, 1, 0, -1, 0],
    [0, 0, -1, 0, 0, 0],
    [0, 0, 0, 0, -1, 1]

]

visted = [[0]*N for _ in range(N)]
print(visted)
dx = [-1,1,0,0]
dy = [0,0,-1,1]


re = solution()

print('re :', re)
#=>
print('==============================')

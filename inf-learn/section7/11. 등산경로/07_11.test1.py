
# DFS

def min_max(kind, list):
    # (kind) 0 : min , 1 : max
    minVal = 2147000000
    maxVal = 0
    x = 0
    y = 0
    for i in range(len(list)):
        for j in range(len(list)):
            if kind == 0 :
                if list[i][j] < minVal:
                    minVal = list[i][j]
                    x = i
                    y = j
            elif kind == 1 :
                if list[i][j] > maxVal:
                    maxVal = list[i][j]
                    x = i
                    y = j
    if kind == 0 :
        return (x, y, minVal)
    elif kind == 1 :
        return (x, y, maxVal)

def DFS(x, y):
    global cnt
    if inp[x][y] == maxVal[2]:
        print('top')
        cnt += 1
    else:
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if 0<=next_x<N and 0<=next_y<N :
                if inp[x][y] < inp[next_x][next_y]:
                    DFS(next_x, next_y)

def solution():
    answer = 0

    visted[minVal[0]][minVal[1]]=1
    DFS(minVal[0],minVal[1])

    return answer

N = 5
inp = [
    [2, 23, 92, 78, 93],
    [59, 50, 48, 90, 80],
    [30, 53, 70, 75, 96],
    [94, 91, 82, 89, 93],
    [97, 98, 95, 96, 100]
]
visted = [[0]*N for _ in range(N)]
print(visted)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

minVal = min_max(0, inp)
maxVal = min_max(1, inp)
cnt = 0

print(minVal, maxVal)

re = solution()
print('cnt', cnt)
print('re :', re)
#=>
print('==============================')

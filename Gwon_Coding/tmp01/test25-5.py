
#

data = [[0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 0, 0, 0, 1, 0],
        [1, 1, 1, 0, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 1, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]]

# 상하좌우 를 살핀다
# 육지 0
ans = 0

def find_0() :
    for i in range(len(data)) :
        for j in range(len(data[0])) :
            if data[i][j] == 0 :
                return i , j
            #print(data[i][j])
    return -1, -1

def dfs(x, y) :
    global ans
    stk = []
    # 호출 한 거 우선 넣고
    stk.append([x, y])
    d_x = [-1,1, 0, 0]   # 상하좌우
    d_y = [0, 0, -1, 1]

    while len(stk) > 0 :
        tx, ty = stk.pop()
        print(tx, ty)
        for i in range(len(d_x)) : # 4방향
            if 0 <= tx + d_x[i] < len(data)  and data[ tx + d_x[i] ] [ty] == 0 :
                stk.append([tx + d_x[i] ,ty])
                data[tx + d_x[i]][ty] = 1
            if 0 <= ty + d_y[i] < len(data)  and data[tx] [ ty + d_y[i] ] == 0 :
                stk.append([tx  ,ty + d_y[i] ])
                data[tx][ty + d_y[i]] = 1
        print(stk)
    ans += 1

# ti, tj = find_0()
# print(ti, tj)
# dfs(ti, tj)

while True :
    ti, tj = find_0()
    print(ti, tj)
    if ti == -1 :
        break
    else :
        dfs(ti, tj)

print(ans)



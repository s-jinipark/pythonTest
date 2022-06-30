
# 2차원 배열에서 하나의 점을 정해주고
# 동서남북으로 1을 추가 ..
# 어디까지 ?


# 5 * 5 배열을 만들고
# [2][2] 에 1을 셋팅
# 동서남북에 1을 셋팅
# 어디까지 ?? 2개 까지


n = 5
tmp = [[0 for i in range(n)] for j in range(n)]
tmp[2][2] = 1
#print(tmp)



dx = [-1,1,0,0] # 상하좌우로
dy = [0,0,-1,1]

# 몇 회 ??
no = 2

# 우선 1 이 셋팅된 pos 를 찾아야 함
posX = 0
posY = 0
for i in range(n):
    for j in range(n):
        if tmp[i][j] == 1 :
            posX = i
            posY = j
#print(posX, posY)

# 샇하좌우로 1을 2번 넣는다
for i in range(1,no+1) :   # (0 부터 시작하면 안됨, 곱해야 되서...)
    for j in range(4) :   # 상하좌우
        newX = posX + dx[j] * i
        newY = posY + dy[j] * i
        print(newX, newY)
        # 범위 chk
        if 0 <= newX < n and 0<= newY < n :
            tmp[newX][newY] = 1

for i in range(n):
    print(tmp[i])
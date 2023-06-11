
print('==============================')

from collections import  deque

arr = [[0] * 4 for _ in range(4)]
arr[1][1] = 1
q = deque()
q.append((1,1))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# => 여기까지가 초기 셋팅

# [2] 일자를 계산하려면
lastNum = 0
lastNum2 = 0

# [3] 씨앗이 두개라면 ??
q.append((2,2))  # 추가하기만 하면 됨

while q:   # while len(q) !=0 : 아렇게 해도 됨
    nowX, nowY = q.popleft()  # [꺼낼 때는 x, y 에 각각]

    for i in range(4):
        nx = nowX + dx[i]
        ny = nowY + dy[i]

        if 0 <= nx < 4 and 0 <= ny < 4 : # [등호 주의]
            if arr[nx][ny] == 0 :
                arr[nx][ny] = arr[nowX][nowY] + 1
                q.append((nx, ny))
                # [2]
                lastNum += 1
                print(lastNum)
                # 이거 그냥 더하니까 15 가 나옴
                lastNum2 = arr[nx][ny]  # [중요] 마지막 값을 넣음
                print('lastNum2:', lastNum2)

print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])

print(lastNum)

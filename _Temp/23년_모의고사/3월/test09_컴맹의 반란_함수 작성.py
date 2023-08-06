
from collections import deque
def solution(n, connect):
    answer = 0

    # 일단 , BFS 로..
    start = 1
    ch = [0] * (n+1)  # index 아니라 번호로 체크하려고

    qu = deque()
    qu.append(start)
    ch[start] = 1
    cnt = 0

    while qu :
        now = qu.popleft()
        cnt += 1
        for i in range(len(connect) ):
            if now == connect[i][0]  and ch[connect[i][1]] == 0:
                qu.append(connect[i][1])
                ch[connect[i][1]] = 1
            elif now == connect[i][1]  and ch[connect[i][0]] == 0 :
                qu.append(connect[i][0])
                ch[connect[i][0]] = 1

    print(cnt)
    return answer


n = 5
connect = [[1, 2], [3, 2], [4, 5]]  # 컴퓨터는 1번부터 차례대로 번호가 매겨지며 영희의 컴퓨터는 1번 컴퓨터입니다.

an = solution(n, connect)
print(an)
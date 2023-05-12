
# n개의 음이 아닌 정수가 있습니다. 이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다.
# 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3

numbers = [1,1,1]

target = 1

tot = 0

N = len(numbers)

# BFS , 큐 이용

from collections import deque

def bfs(n):
    answer = 0
    qu = deque()
    qu.append([numbers[0], 0])
    qu.append([-1 * numbers[0], 0])

    while len(qu) > 0 :
        temp, idx = qu.popleft()
        idx += 1
        print('[', temp, ',', idx, '] pop')
        if idx < N :
            qu.append([temp+numbers[idx], idx])
            qu.append([temp-numbers[idx], idx])
            print(qu)
        else :
            if temp == target :
                print('>', qu)
                answer += 1
    return answer

ans = bfs(0)
print(ans)


# index 를 주고 넣는데, 결국 N 과 같은 index 가 나오면 그제서야 target 값과 비교
# index 가 맞지 않는 애들은 걍.. 중간 단계 임


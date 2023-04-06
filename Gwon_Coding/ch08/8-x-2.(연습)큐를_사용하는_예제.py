
from collections import deque

N = 6
'''
N 장의 카드 (각각의 카드는 차례로 1부터 N까지.. 1번 맨위)

한장 남을 때까지 반복
제일 위 카드를 바닥에 버린다
그 다음 제일 위 카드를 제일 아래로...
'''
qu = deque()

for i in range(1, N+1):
    qu.append(i)

print(qu)
while len(qu) > 1 :
    qu.popleft()
    qu.append(qu.popleft())

print(qu)

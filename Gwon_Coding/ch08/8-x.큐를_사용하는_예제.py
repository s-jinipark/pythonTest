
from collections import deque

N = 4

queue = deque()

# for i in range(1, N+1):
#     queue.append(i)
# 1번 카드가 맨 위
for i in range(N):
    queue.append(N-i)

print(queue)

'''
카드가 한장 남을 때까지 반복
 1. (홀) 제일 위에 있는 카드를 바닥에 버린다
 2. (짝) 제일 위에 있는 카드를 제일 아래에 ..

( cnt 1 로 셋팅하고  홀/짝 다르게 수행)
'''
# cnt = 1
# while (len(queue) > 1) :
#     연습 = queue.popleft()
#     if cnt%2 == 0 :  # 짝수
#         queue.append(연습)
#     cnt += 1
# print(queue)

print("--------------------")
'''
  이거 뭐 홀짝 나눌 필요 없이 연달아 하면 됨
  제일 위를 뽑는 거임 -> 잘 읽어야 될 듯
'''
while len(queue) > 1 :
    queue.pop()
    queue.appendleft(queue.pop())
    #print(queue)

print(queue)
print(queue.popleft())
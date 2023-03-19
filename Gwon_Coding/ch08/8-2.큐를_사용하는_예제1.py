
# 큐를 통해 사용하는 기능은  6 가지
# 1. push : 데이터를 큐에 추가한다 (전단부터 후단으로 차곡차곡 쌓는다)
# 2. pop : 큐의 가장 앞 단 데이터를 삭제한다
# 3. size : 큐에 데이터가 몇 개 들어 있는지 확인한다
# 4. empty : 큐가 비어 있는지 확인한다
# 5. front : 큐의 가장 앞 데이터가 무엇인지 확인한다
# 4. backs : 큐의 가장 뒤 데이터가 무엇인지 확인한다

import sys
from collections import deque

sys.stdin = open("input8-2.txt", "rt")
n = int(input())  # n

command = []
for i in range(n):
   command.append(input())

print(command)

queue = deque([])  # 이렇게 ?

# for i in range(n):
#     tmp_comm_arr = command[i].split()
#     if tmp_comm_arr[0] == 'push' :
#         queue.append(tmp_comm_arr[1])
#     elif tmp_comm_arr[0] == 'pop' :
#         #if len(queue) == 0 :
#         if not queue :  # 책엔 이렇게 하네...
#             print(-1)
#         else :
#             #print(queue.pop())  # 이거는 스택같이 됨
#             print(queue.popleft())
#     elif tmp_comm_arr[0] == 'size' :
#         print( len(queue) )
#     elif tmp_comm_arr[0] == 'empty' :
#         if not queue :  # 책엔 이렇게 하네...
#             print(1)
#         else :
#             print(0)
#     elif tmp_comm_arr[0] == 'front' :
#         if not queue :  # 책엔 이렇게 하네...
#             print(-1)
#         else :
#             print(queue[0])
#     elif tmp_comm_arr[0] == 'back' :
#         if not queue :  # 책엔 이렇게 하네...
#             print(-1)
#         else :
#             print(queue[-1])

#print(queue)

'''
배열로도 할 수 있는데 왜 큐를 써야 하지?
배열을 이용하여 큐의 기능을 구현한다면 먼저 삽입된 데이터가 삭제될 때마다
ㅇ(데이터의 크기) 가 소요되기 때문 
'''


'''
연습
 ○ push X : 정수 X 를 큐에 넣는 연산이다
 ○ pop : 큐에 가장 앞에 있는 정수를 빼고, 그 수를 출력한다
    만약 큐에 들어 있는 정수가 없는 경우에는 -1 을 출력한다
 ○ size : 큐에 들어있는 정수의 개수를 출력한다
 ○ empty : 큐가 비어 있으면 1, 아니면 0 을 출력한다
 ○ front : 큐의 가장 앞에 있는 정수를 출력한다. 없으면 -1
 ○ back : 큐의 가장 뒤에 있는 정수를 출력한다. 없으면 -1
 
'''

for i in range(n):
    #print(command[i])
    tmp_cmd = command[i].split()
    if tmp_cmd[0] == 'push' :
        queue.append(tmp_cmd[1])
    elif tmp_cmd[0] == 'pop' :
        if queue :
            print(queue[0])
            queue.popleft()
        else :
            print(-1)
    elif tmp_cmd[0] == 'size' :
        print(len(queue))

    elif tmp_cmd[0] == 'empty' :
        if queue :
            print(0)
        else :
            print(1)
    elif tmp_cmd[0] == 'front' :
        if queue :
            print(queue[0])
        else :
            print(-1)
    elif tmp_cmd[0] == 'back' :
        if queue :
            print(queue[-1])
        else :
            print(-1)
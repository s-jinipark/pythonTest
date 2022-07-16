
# 큐를 통해 사용하는 기능은  6 가지
# 1. push : 데이터를 큐에 추가한다
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

for i in range(n):
    tmp_comm_arr = command[i].split()
    if tmp_comm_arr[0] == 'push' :
        queue.append(tmp_comm_arr[1])
    elif tmp_comm_arr[0] == 'pop' :
        #if len(queue) == 0 :
        if not queue :  # 책엔 이렇게 하네...
            print(-1)
        else :
            #print(queue.pop())  # 이거는 스택같이 됨
            print(queue.popleft())
    elif tmp_comm_arr[0] == 'size' :
        print( len(queue) )
    elif tmp_comm_arr[0] == 'empty' :
        if not queue :  # 책엔 이렇게 하네...
            print(1)
        else :
            print(0)
    elif tmp_comm_arr[0] == 'front' :
        if not queue :  # 책엔 이렇게 하네...
            print(-1)
        else :
            print(queue[0])
    elif tmp_comm_arr[0] == 'back' :
        if not queue :  # 책엔 이렇게 하네...
            print(-1)
        else :
            print(queue[-1])

#print(queue)

'''
배열로도 할 수 있는데 왜 큐를 써야 하지?
배열을 이용하여 큐의 기능을 구현한다면 먼저 삽입된 데이터가 삭제될 때마다
O(데이터의 크기) 가 소요되기 때문 
'''
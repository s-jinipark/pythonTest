
from collections import deque

# deque

data = deque([2,3,4])

data.appendleft(1)
print(data)

data.append(5)
print(data)

data.popleft()
print(data)

data.pop()
print(data)

'''
[deque 함수]

popleft() : 첫 번째 데이터 삭제
pop() : 마지막 데이터 삭제
appendleft(x) : 첫 번째 인덱스에 데이터 x를 삽입
append() : 마지막 인덱스에 데이터 x를 삽입

 
deque를 큐로 활용할 때 : 선입선출  

데이터 삽입 : append() 
데이터 삭제 : popleft()

 
deque를 스택으로 활용할 때 : 후입선출 

데이터 삽입 : append() 
데이터 삭제 : pop()

'''



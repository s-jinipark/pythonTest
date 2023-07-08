##########
# 스택
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)
# 거꾸로 출력
print(stack[::-1])


##########
# 큐
from collections import deque

qu = deque()  # 이걸로 사용
qu.append(5)
qu.append(2)
qu.append(3)
qu.append(7)
qu.popleft()
qu.append(1)
qu.append(4)
qu.popleft()

print(qu)
qu.reverse()
print(qu)


##########
# 재귀함수
# def recursive_func():
#     print('재귀함수 호출')
#     recursive_func()

#recursive_func()
# 오류 발생
# RecursionError: maximum recursion depth exceeded while calling a Python object


##########
# 재귀함수2 - 종료 조건
# def recursive_func(i):
#     if i > 100 :
#         return
#     print(i , '번째 재귀함수에서', i+1, '번째 재귀함수를 호출 합니다.')
#     recursive_func(i+1)
#     print(i , '번째 재귀함수 종료')
#
# recursive_func(1)



def factorial(n):
    global  tmp
    if n <= 1 :
        return 1
    else :
        #연습 += n
        return  n * factorial(n-1)

tmp = factorial(5)
print(tmp)

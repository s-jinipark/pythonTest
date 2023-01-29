
# 문제 001 > 숫자의 합 구하기
#

num = int(input())
print(num)

# 123 을 입력했다고 가정
# lst = map(int, input().split())
# print(list(lst)) # ->  [123]

# 헐 그냥 리스트로 변환하면 됨?
# lst = list(input())
# print(lst)  # -> ['1', '2', '3']

lst = list(map(int, input()))
print(lst)  # -> [1, 2, 3] (원하던 거 임)

sum = 0

for i in lst:
    sum = sum + i
print(sum)

'''
실행 예
>5
5
>54321
[5, 4, 3, 2, 1]
15
'''

print("1. 하나를 입력 받기")
#num = int(input())
#print(num)

print("2. 한줄을 입력 받기")
# 입력 : 3 5
# a, b = map(int, input().split())
# print(a, b)
# -> 출력 : 3 5

print("3. 리스트를 통해 한줄을 입력 받기")
# 입력 : 1 2 3 4 5 6 7
# num = list(map(int, input().split()))
# print(num)
# -> 출력 : [1, 2, 3, 4, 5, 6, 7]

print("4. 한 줄로 문자열 변수 여러 개를 입력 받기")
# [문자열이라 여긴 map 없이..]
# 입력 : abc def
# a, b = input().split()
# print(a, b)
# -> 출력 : abc def

print("5. 문자열 여러 줄을 입력 받기 1")
# 입력 : ABCDEF
#       BCDEFA
#       CDEFAB
#str=[input() for _ in range(3)]
#print(str)
# -> 출력 : ['ABCDER', 'BCDEFA', 'CDEFAB']

print("6. 문자열 여러 줄을 입력 받기 2")
# 한 줄에 띄어쓰기 없이 정수를 여러개 받았을 때, 2차원 배열 형태로 저장하는 방법
# 입력 : 0101
#       1010
#       0101
#       1010
# arr=[list(map(int,input())) for _ in range(4)]
# print(arr)
# -> 출력 : [[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]]

print("7. 2차원 배열을 입력 받기")
# 한 줄에 띄어쓰기가 있는 배열을, 여러개의 줄을 통해 입력받을 때
# 입력 : 1 2 3 4 5
#       6 7 8 9 10
#       5 4 3 2 1
#변수명=[list(map(int,input().split() )) for _ in range(3)]
#=> .split() 이 있다는 점

lst = [list(map(int, input().split())) for _ in range(3)]
print(lst)
# -> 출력 : [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [5, 4, 3, 2, 1]]


print("1. 하나를 입력 받기")
#num = int(input())
#print(num)

print("2. 한줄을 입력 받기")
# 입력 : 3 5
#a, b = map(int, input().split())
#print(a, b)

print("3. 리스트를 통해 한줄을 입력 받기")
# 입력 : 1 2 3 4 5 6 7
#num = list(map(int, input().split()))
#print(num)

print("4. 한 줄로 문자열 변수 여러 개를 입력 받기")
# 입력 : abc def
#a, b = input().split()
#print(a, b)

print("5. 문자열 여러 줄을 입력 받기 1")
# 입력 : ABCDEF
#       BCDEFA
#       CDEFAB
#str=[input() for _ in range(3)]
#print(str)

print("6. 문자열 여러 줄을 입력 받기 2")
# 입력 : 0101
#       1010
#       0101
#       1010
arr=[list(map(int,input())) for _ in range(4)]
print(arr)  # -> [[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]]

print("7. 2차원 배열을 입력 받기")
# 입력 : 1 2 3 4 5
#       6 7 8 9 10
#       5 4 3 2 1


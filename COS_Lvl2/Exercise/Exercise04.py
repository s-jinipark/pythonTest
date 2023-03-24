
# 백트래킹 카테고리
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
#   1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

from itertools import permutations
N, M = 3, 1
print( N, M )
olist = [1,2,3]
lst = list(permutations(olist, M))
print(lst)
# 값이 이렇게 나옴 [(1,), (2,), (3,)]
# 위는 구현 시
print('-----')

#n, m = list(map(int, input().split()))
n, m = 3, 2
s = []

def dfs():
  if len(s) == m:  # 리스트에 들어간 수열들이 m개가 되면 리스트에 들어있는 숫자들을 모두 출력하고 함수를 나온다.
    print(' '.join(map(str, s)))
    return

  for i in range(1, n + 1):  # for문을 이용하여 1부터 n까지의 숫자들을 모두 확인
    if i not in s:  # 리스트 s 중복여부 확인
      s.append(i)   # 중복이 아니면 숫자 i를 리스트 s에 넣기
      print(s)
      dfs()         #  현재 s=[1]인 상태에서 다음숫자를 넣기위하여 가지치기하기(재귀함수)
      s.pop()

dfs()


# # 일단 4개짜리..
# # dfs 로 전체 chk 하는거 만들고
# # 중간에 빠질 수 있게...
#
#
# SIZE = 4
# # visited 와는 다르지만, 유사
# x = [0] * SIZE # 각 좌표를 넣어줌.
# cnt = 0
#
# def is_free(ix, iy):  # 0 0 -> 0 1  -> 1 1
#   for i in range(iy):
#     if x[i] == ix or abs(x[i]-ix) == abs(i-iy):
#       return False
#       # 1) 같은 열에 다른 퀸이 있는 경우
#       # 2) 왼쪽 대각선, 오른쪽 대각선에 다른 퀸이 있는 경우.
#
#   return True
#
# def queen(n):
#   global cnt
#   if n == SIZE :
#     print('**')
#     print(x)
#     cnt += 1
#   else :
#     # 여기에 검사하는 로직
#     # 없다면 다 출력하겠지 ?
#     # queen(n+1)
#     # print(x)  #  => 이렇게 하면 4번만 출력
#     # [2]
#     # for i in range(SIZE):
#     #   x[n] = i
#     #   #print(x)
#     #   queen(n+1)  #  => 이렇게 하면 [0,0,0,0] 부터 [3,3,3,3] 까지 256 번 출력
#     for i in range(SIZE):
#       if is_free(i, n) :   # x, y 순 ?
#         x[n] = i
#         #print(x)
#         queen(n+1)
#
# queen(0)
#
# print(cnt)
# # 참조 : https://seongonion.tistory.com/103

# --------------------------------------------------
# # NQueen
# # backtracking
#
# def printQueen():
#   global cnt
#   print("%d번째 경우" % cnt)
#
#   if SIZE == 4:
#     print("+--------+")
#   if SIZE == 8:
#     print("+----------------+")
#
#   for i in range(SIZE):
#     print("|",end="")
#     for j in range(SIZE):
#       if j == x[i]:
#         print("<>",end="")
#       else:
#         print("  ",end="")
#     print("|")
#
#   if SIZE == 4:
#     print("+--------+")
#   if SIZE == 8:
#     print("+----------------+")
#
# def is_free(ix, iy):  # 최조 0 0 -> 0 1  -> 1 1
#   for i in range(iy):
#     if x[i] == ix or abs(x[i]-ix) == abs(i-iy):
#       return False
#   return True
#
# def queen(n):      # dfs 와 유사
#   global cnt, x
#   print(x)
#   if n == SIZE:  # 끝까지 온 경우..
#     cnt +=1
#     #printQueen()   # 참고용 출력   4와 8인 경우 퀸 위치 확인용
#     print("**", x)
#   else:
#     for i in range(SIZE):  # 0 1 2 3
#       if is_free(i, n):  # 해당 위치에 퀸을 놓을 수 있는지 없는지 is_free 함수를 통해서 판단한다.
#         x[n] = i  # 퀸을 [n, i] 위치에 놓겠다
#         queen(n+1)  # 퀸을 놓을 수 있어야 다음으로 가는 거.. !!
#
#
# SIZE = 4
# cnt = 0
# x = [0 for i in range(SIZE)]   # 1차원 이라는 ...
# queen(0)
# print(cnt)
#
# # SIZE = 8
# # cnt = 0
# # x = [0 for i in range(SIZE)]
# # queen(0)
# # print(cnt)


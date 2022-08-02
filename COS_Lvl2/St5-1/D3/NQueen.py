# NQueen
# backtracking

def printQueen():
  global cnt
  print("%d번째 경우" % cnt)

  if SIZE == 4:
    print("+--------+")
  if SIZE == 8:
    print("+----------------+")

  for i in range(SIZE):
    print("|",end="")
    for j in range(SIZE):
      if j == x[i]:
        print("<>",end="")
      else:
        print("  ",end="")
    print("|")

  if SIZE == 4:
    print("+--------+")
  if SIZE == 8:
    print("+----------------+")


def is_free(ix, iy):  # 0 0 -> 0 1  -> 1 1
  for i in range(iy):
    if x[i] == ix or abs(x[i]-ix) == abs(i-iy):
      return False
  return True

def queen(n):
  global cnt, x
  print(x)
  if n == SIZE:
    cnt +=1
    #printQueen()   # 참고용 출력   4와 8인 경우 퀸 위치 확인용
  else:
    for i in range(SIZE): # i 는 0 부터 size
      if is_free(i, n):
        x[n] = i
        queen(n+1)



SIZE = 4
cnt = 0
x = [0 for i in range(SIZE)]  # 1차원으로 시작
queen(0)
print(cnt)

# SIZE = 8
# cnt = 0
# x = [0 for i in range(SIZE)]
# queen(0)
# print(cnt)


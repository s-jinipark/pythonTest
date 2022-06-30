def rightrotation90(data):
  size = len(data)
  rightrotation = [[0 for i in range(size)] for j in range(size)]

  for i in range(size):
    for j in range(size):
      rightrotation[i][j] = data[size - 1 - j][i]

  return rightrotation

def leftrotation90(data):
  size = len(data)
  leftrotation = [[0 for i in range(size)] for j in range(size)]

  for i in range(size):
    for j in range(size):
      leftrotation[i][j] =  data[j][size - 1 - i]

  return leftrotation


def rotation180(sample):
  size = len(sample)
  new180 = [[0 for i in range(size)] for j in range(size)]

  for i in range(size):
    for j in range(size):
      new180[i][j] = sample[size - 1 - i][size - 1 - j]

  return new180




def printList(sample):
  for ary in sample:
    for c in ary:
      print(c, end=" ")
    print()
  print()


data = [[5, 7, 8, 2, 3],
        [8, 1, 4, 3, 8],
        [6, 4, 3, 7, 9],
        [1, 5, 2, 7, 4],
        [8, 7, 4, 3, 9]]

print("원본")
printList(data)

print("오른쪽 90도 회전")
res1 = rightrotation90(data)
printList(res1)

print("왼쪽 90도 회전")
res2 = leftrotation90(data)
printList(res2)

print("오른쪽 180도 회전")
res2 = rotation180(data)
printList(res2)


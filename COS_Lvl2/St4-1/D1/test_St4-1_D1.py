
def rightrotation90(data):
    tmp_len = len(data)
    tmp = [[0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]]

    for i in range(tmp_len):
        for j in range(len(data[0]) ):
            #print(i, j)
            tmp[j][tmp_len-1-i] = data[i][j]
    return tmp

def leftrotation90(data):
    tmp_len = len(data)
    tmp = [[0 for i in range(tmp_len)] for j in range(tmp_len)]
    #print(연습)
    for i in range(tmp_len):
        for j in range(tmp_len):
            tmp[tmp_len-1-j][i] = data[i][j]
    return tmp

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

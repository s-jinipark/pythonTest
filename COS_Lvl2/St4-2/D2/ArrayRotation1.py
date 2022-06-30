def solution(sample):
    #answer = []
    tmp_len = len(sample)
    tmp_180 = [[0 for _ in range(tmp_len)] for _ in range(tmp_len)]
    tmp_s_180 = [[0 for _ in range(tmp_len)] for _ in range(tmp_len)]
    answer = [[0 for _ in range(tmp_len)] for _ in range(tmp_len)]

    # 180 회전
    for i in range(tmp_len) :
        for j in range(tmp_len) :
            tmp_180[i][tmp_len-1-j] = sample[i][j]
    #printList(tmp_180)

    # 대각선 180 회전
    for i in range(tmp_len) :
        for j in range(tmp_len) :
            tmp_s_180[tmp_len-1-j][tmp_len-1-i] = sample[i][j]
    #printList(tmp_s_180)

    # 대각선 180 회전
    for i in range(tmp_len) :
        for j in range(tmp_len) :
            if tmp_180[i][j] + tmp_s_180[i][j] > 10 :
                answer[i][j] = (tmp_180[i][j] + tmp_s_180[i][j])%10
            else :
                answer[i][j] = tmp_180[i][j] + tmp_s_180[i][j]
    #printList(answer)

    return answer

'''
한번 그려 봤음

[0][0]    [0][3]
[0][1]    [0][2]
[0][2]    [0][1]
[0][3]    [0][0]
[1][0]    [1][3]
[1][1]    [1][2]
...

[0][0]    [3][3]
[0][1]    [2][3]
[0][2]    [1][3]
[0][3]    [0][3]
[1][0]    [3][2]
[1][1]    [2][2]
...

루프돌면서 180 도 는 행마다 j 만 바꿔주면 되고
대각선 180도는 i -> j 로 가는데 max 에서 i 빼주는 걸로
             j -> i 로 가면서 반대로..

'''


# 행렬 출력 확인용
def printList(sample):
  for ary in sample:
    for c in ary:
      print(c, end=" ")
    print()
  print()

# sample1
data = [[3,7,1,9],
        [5,2,6,8],
        [6,4,7,1],
        [5,7,5,4]]
res = solution(data)
printList(res)


# sample2
data = [[6,3,7,2,9],
        [8,5,3,6,7],
        [1,6,8,7,1],
        [4,5,7,9,4],
        [7,6,3,7,5]]
res = solution(data)
printList(res)

# sample3
data = [[6,3,7,2,9,5,3,7],
          [3,6,8,8,5,3,6,7],
          [1,6,4,3,8,8,7,1],
          [6,4,5,7,5,2,9,4],
          [7,4,8,6,3,1,7,5],
          [5,6,3,9,8,2,7,1],
          [6,3,5,7,8,2,6,1],
          [2,4,4,9,6,1,2,5]]
res = solution(data)
printList(res)



# 프로그래머스 스타일 로 ...
def solution(N, inp, M, chg):
    answer = 0
    for c in chg:
        print(c)
        # 인덱스를 +/- 하는데 max/min 를 넘으면 순환하도록...
        sign = 1
        if c[1] == 0 :
            sign = -1
        #tmp_row = inp[c[0]-1]
        # OMG 이거 deep copy 해야 하는 듯
        tmp_row = []
        for t in range(N):
            tmp_row.append(inp[c[0]-1][t])
        print(tmp_row)
        for i in range(N):
            tmp = i + (c[2]*sign)
            if tmp > N-1 :
                tmp = tmp % N
            if tmp < 0 :
                tmp = N + tmp  # 아래처럼 적어보고 도출
            print(i , '->', tmp)
            inp[c[0]-1][tmp] = tmp_row[i]
        print(inp[c[0]-1])
    print(chg)

    '''
    첫번째 시도 , 오른쪽은 되는데, 왼쪽이 안되는 듯..
    (왼쪽 3)
    0 -3 (2 가 되야.)
    1 -2 (3 이 되야.)
    2 -1 (4 가 되야.)
    3 0
    4 1
    '''
    print(inp)

    # 모래시게 모양
    mid = N//2
    print('mid :' , mid)
    # start 와 end 를 찍어 봄
    for i in range(N):
        print(i, N-1-i)
        if i < mid :
            start = i
            end = N-1-i
        else :
            start = N-1-i
            end = i
        for j in range(start, end+1):
            print('>', i, j)
            answer += inp[i][j]

    return answer

N = 5
inp = [
[10,13,10,12,15],
[12,39,30,23,11],
[11,25,50,53,15],
[19,27,29,37,27],
[19,13,30,13,19]
]
M = 3
chg = [  # 첫 : 행번호  , 두 : 방향 (0 : 왼쪽, 1 : 오른쪽), 세 : 회전하는 격자의 수
[2,0,3],  # 행 번호는 1부터 시작...
[5,1,2],
[3,1,4]
]
re = solution(N, inp, M, chg)
print('re :', re)
#=> 362
print('==============================')

N = 7
inp = [
[74,10,31,26,59,16,89],
[78,44,49,1,64,33,15],
[9,95,70,18,22,25,40],
[62,77,28,3,78,75,23],
[82,38,20,16,42,1,79],
[1,24,2,25,95,26,79],
[4,35,46,94,70,44,83]
]
M = 3
chg = [  # 첫 : 행번호  , 두 : 방향 (0 : 왼쪽, 1 : 오른쪽), 세 : 회전하는 격자의 수
[2,0,3],  # 행 번호는 1부터 시작...
[5,1,2],
[3,1,4]
]
re = solution(N, inp, M, chg)
print('re :', re)
#=> 1304
print('==============================')

N = 9
inp = [
[64,8,59,87,94,71,66,4,9],
[38,21,30,24,33,65,7,79,27],
[99,10,78,74,84,32,33,74,30],
[4,6,69,53,100,15,23,15,88],
[22,88,8,3,62,75,46,4,41],
[39,64,7,75,91,26,83,32,41],
[100,98,20,100,18,39,90,60,56],
[56,30,94,29,81,76,96,50,11],
[66,88,88,95,13,56,29,13,31]
]
M = 5
chg = [  # 첫 : 행번호  , 두 : 방향 (0 : 왼쪽, 1 : 오른쪽), 세 : 회전하는 격자의 수
[1,0,5],
[3,0,6],
[2,1,5],
[6,0,7],
[5,0,8]
]
re = solution(N, inp, M, chg)
print('re :', re)
#=> 2539
print('==============================')

N = 17
inp = [
[33,20,70,4,10,50,75,39,29,52,21,92,57,71,48,65,78],
[60,87,16,63,37,39,98,23,58,25,25,36,64,97,56,28,43],
[11,13,8,97,34,54,50,42,67,59,79,93,48,62,97,18,58],
[56,9,38,68,7,49,52,37,41,28,6,36,88,78,67,45,42],
[69,1,71,75,64,7,8,41,55,51,88,80,35,50,22,45,51],
[32,79,43,11,77,24,100,33,59,26,37,37,52,92,62,46,32],
[5,40,45,34,75,35,23,86,27,94,19,95,18,96,37,65,99],
[82,14,22,50,27,7,92,20,99,8,19,40,98,86,41,42,91],
[23,9,38,92,17,24,15,89,57,93,52,81,9,28,10,3,1],
[1,19,69,31,58,95,77,36,58,81,1,97,95,4,80,97,51],
[67,57,65,42,50,56,66,79,66,63,77,28,46,63,1,67,39],
[35,44,19,73,51,11,90,75,77,47,76,4,36,48,40,71,98],
[21,29,52,28,8,63,41,27,72,59,60,57,80,5,49,16,50],
[93,70,6,68,68,21,90,37,83,38,23,3,95,62,38,71,24],
[63,8,26,76,60,48,23,56,28,90,20,25,66,37,82,42,52],
[2,19,78,20,97,58,96,22,16,30,62,19,94,27,50,74,45],
[37,90,41,63,21,11,42,73,49,45,70,6,99,48,37,38,57]
]
M = 10
chg = [  # 첫 : 행번호  , 두 : 방향 (0 : 왼쪽, 1 : 오른쪽), 세 : 회전하는 격자의 수
[11,0,13],
[15,0,12],
[13,1,13],
[7,0,7  ],
[6,1,6  ],
[16,0,16],
[9,0,9  ],
[8,1,8  ],
[12,1,12],
[1,1,1  ]
]
re = solution(N, inp, M, chg)
print('re :', re)
#=> 8119
print('==============================')
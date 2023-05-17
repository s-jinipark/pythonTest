
# 확인 필요

def beauti_prt(x):
    for i in range(len(x)):
        print (x[i])
    print()

# 프로그래머스 스타일 로 ...
def solution(N, inp):
    answer = 0
    # 자신의 상하좌우 숫자보다 큰 숫자
    dx = [-1, 1, 0, 0] # 상하
    dy = [0, 0, -1, 1] # 좌우  #=> 여기서는 x/y 가 행/열

    # 테두리를 친다
    #tmp = [[0]*(N+2)] *(N+2)  # OMG 이렇게 하면 안됨!!
    tmp = [[0 for _ in range(N+2)] for _ in range(N+2)]
    print(tmp)
    for i in range(N):
        for j in range(N):
            #print(inp[i][j], i, j, i+1, j+1)
            tmp[i+1][j+1] = inp[i][j]

    #print(tmp)
    beauti_prt(tmp)
    for i in range(1, N+1):
        for j in range(1, N+1):
            #print(i, j)
            bon = tmp[i][j]
            # 상하좌우 비교
            for k in range(4):
                comp = tmp[i+dx[k]][j+dy[k]]
                #print(bon, comp)
                if bon < comp :
                    break
            else:   # 여기 point
                answer +=1
                print(bon, ':', i, j)

    return answer

N = 5
inp = [
[5,3,7,2,3],
[3,7,1,6,1],
[7,2,5,3,4],
[4,3,6,4,1],
[8,7,3,5,2]
]

re = solution(N, inp)
print('re :', re)
#=>
print('==============================')

N = 7
inp = [
[27,33,80,73,19,23,15],
[48,84,61,3,36,9,62],
[87,57,3,14,69,17,22],
[17,57,86,21,85,51,82],
[7,94,66,21,19,41,82],
[27,5,59,28,26,77,64],
[5,46,4,63,76,99,8]
]

re = solution(N, inp)
print('re :', re)
#=> 11
print('==============================')
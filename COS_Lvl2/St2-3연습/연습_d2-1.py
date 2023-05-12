
# 확인 필요 (다시 볼것)

def prtRes(res):
    for i in range(len(res) ):
        for j in range(len(res[0])) :
            print(res[i][j], end=' ')
        print()


def solution(N, start):
    answer = 0
    # 코드를 작성하세요.
    #result = [ [0]*(N) ] * (N)
    result = [[0 for _ in range(N)] for _ in range(N)]
    # 2차원 배열 이렇게 선언해야 함

    #print(result)
    prtRes(result)

    length = N
    num = start
    direction = 1
    x = 0
    y = -1  #0
    cnt = 0
    while(True) :
        for i in range(length):
            #y = i * direction
            y += direction
            #print(x, y)
            result[x][y] = num
            num += 1

        length -= 1
        if length < 0:
            break

        for i in range(length):
            #x = j * direction
            x += direction
            #print(x, y)
            result[x][y] = num
            num += 1

        direction *= -1
        # cnt +=1
        # if cnt > 0 :
        #     break
    prtRes(result)
    return answer



# def solution(N, start):
#     answer = 0
#     # 코드를 작성하세요.
#
#     # 일단 0 으로 셋팅
#     result = [[0 for _ in range(N)] for _ in range(N)]
#     print(result)
#
#     num = N  # 갯수를 줄여갈 예정
#     x = 0
#     y = -1
#     direction = 1
#
#     #while True :
#     while start < 100:
#         for i in  range(num):
#             #y += 1   # 아래 for 에서 index err 방지 위해 미리 +1 해준다
#                      # 덕분의 위에 초기값도 0 에서 -1 로 변경
#             y += direction  # 번갈아서 +1 , -1 해줘야 함으로..
#             result[x][y] = start
#             start += 1
#             if x == y :
#                 answer += result[x][y]
#         print(result)
#         num -= 1  # 채울 칸이 줄어 든다
#         if num < 0 :  # 계속 줄어들다가 0 보다 작아지면 stop
#             break
#
#         for j in range(num) :
#             #x += 1
#             x += direction
#             result[x][y] = start
#             start += 1
#             if x == y :
#                 answer += result[x][y]
#         print(result)
#         direction *= -1  # 방향을 바꿔주는 역할
#
#     return answer


N = 6
start = 1
res = solution(N, start)
print(res)              # 128

N = 5
start = 1
res = solution(N, start)
print(res)             # 73



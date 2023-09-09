
##### 최대점수 구하기(DFS)

def DFS(v, point, time):
    global  top_point
    if v == N :  # 종료 조건
        if time <= M:
            print(point)
            if top_point < point :
                top_point = point
    else :
        DFS(v+1, point+inp[v][0], time+inp[v][1])
        DFS(v+1, point, time )

def solution():
    answer = 0
    #print(inp)

    '''
    상태트리
    5개 쓰냐 안쓰냐.. 하면 될 듯
    '''
    DFS(0, 0, 0)
    print('>', top_point)
    return answer

N = 5   # 문제의 개수
M = 20  # 제한 시간

inp = [
    (10,5),  # 점수, 시간
    (25,12),
    (15,8),
    (6,3),
    (7,4)
]

rtn = ''
top_point = 0
re = solution()
print(re)
#=>
print('====================')


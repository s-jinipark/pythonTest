
##### 휴가(삼성 SW역량평가 기출문제 : DFS활용)

def DFS(v, day, point):
    if v == N:  # 종착점
        print(point)
    else:
        for i in range(day, N+1):
            DFS(v+1, i, point+inp[i][1])

def solution():
    answer = 0

    '''
    상태 트리
    N개 쓰냐 안쓰냐.. 하면 안될 거 같아보임
    N가닥으로 뻗는.. 그럼 ? 종료조건은 ?
    
    '''
    DFS(0, 0, 0)
    print('>', top_point)
    return answer

N = 7   # 개수

inp = [
    (4,20),  # 1 일부터 N 일
    (2,10),
    (3,15),
    (3,20),
    (2,30),
    (2,20),
    (2,10)
]

rtn = ''
top_point = 0
re = solution()
print(re)
#=>
print('====================')


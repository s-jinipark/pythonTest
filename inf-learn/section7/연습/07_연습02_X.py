
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
    #DFS(0, 0, 0)
    # -> 오류 나서
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
    (1,10)
]

rtn = ''
top_point = 0
re = solution()
print(re)
#=>
print('====================')

'''
풀이 듣고 다시 풀어 봄
'''
def DFS2(L, sum):
    global  top_point2
    if L == N+1 :
        print(sum)
        if top_point2 < sum:
            top_point2 = sum
    else:
        # 선택 하느냐, 안 하느냐
        if L+inp[L][0] <= N+1:  # if 가 있다는게 기존과 조금 다름
            DFS2(L+inp[L][0], sum+inp[L][1])
        DFS2(L+1, sum)  # L+1 로 다음 거..

def solution2():
    answer = 0
    inp.insert(0,(0,0))  # 0 을 앞에 넣어 줌
    print(inp)

    DFS2(1, 0)  # L, sum
    print('top_point2', top_point2)
    return answer

top_point2 = 0
re2 = solution2()
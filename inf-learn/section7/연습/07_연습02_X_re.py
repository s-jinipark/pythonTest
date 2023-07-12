
##### 휴가(삼성 SW역량평가 기출문제 : DFS활용)

def DFS(L, sum):
    global  res
    if L == N+1:
        print(sum)
        if res < sum:
            res = sum
    else:
        if L+T[L] <= N+1:
            DFS(L+T[L], sum+P[L])  # 다음 상담으로 가는 것(중요)
        DFS(L+1, sum)

def solution():
    answer = 0

    '''
    상태 트리
    N개 쓰냐 안쓰냐.. or  N가닥으로 뻗는.. 헷갈려 하다가...
    
    강의 듣고...
    N 개 쓰냐 안쓰냐.. 하면서
    
    '''
    for i in range(N):
        a, b = inp[i]
        T.append(a)
        P.append(b)
    #print(T,P)
    T.insert(0,0)   # 맨앞에 0 을 넣어줌. index 를 날짜로 쓸려고.. 1부터
    P.insert(0,0)
    print(T,P)

    DFS(1, 0)
    print('res', res)
    return answer

N = 7   # 개수

T=list()
P=list()
inp = [
    (4,20),  # 1 일부터 N 일
    (2,10),
    (3,15),
    (3,20),
    (2,30),
    (2,20),
    (1,10)
]
res = 0
rtn = ''

re = solution()
print(re)
#=>
print('====================')


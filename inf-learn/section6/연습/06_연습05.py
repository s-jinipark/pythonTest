
##### 바둑이 승차(DFS)

def DFS(L,sum):
    global  Max
    #[2] 여기서 cut 하는 걸로
    if sum > C :
        return
    if L == N :
        print(sum)
        if sum > Max :
            Max = sum
        # [2] sum 이 넘으면 위에서 cut
        # if sum <= C and sum > Max :
        #     Max = sum
    else:
        DFS(L+1, sum+inp[L])  # 참여 시킨다
        DFS(L+1, sum)   # 참여시키지 않겠다

def solution():
    answer = 0
    '''
    앞 04 번과 마찬가지로
    상태트리 사용 y 냐, n 냐 에 따라 뻗으면 될 듯...
    sum 을 더해서, max 에 최대 가깝게...
    
    ???
    앞의 이분 검색하고, 문제가 구분이 잘 안 감.
    
    '''
    DFS(0, 0)
    print('Max', Max)
    return answer

C = 259  # max 값이라고 보면됨
N = 5  # 바둑이 수

inp = [81, 58, 42, 33, 61]
Max = 0  # 해설에서는 -2147000000 (0 여섯개)

re = solution()
print(re)
#=>
print('====================')


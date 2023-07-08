
##### 합이 같은 부분집합(DFS : 아마존 인터뷰)

def DFS(v):
    if v == N+1 :
        # 여기서 출력
    else :
        for i in range(N):
            ch[i] =1
            DFS

def solution():
    answer = 0
    '''
    마찬가지로 상태 트리를 그려서 사용하냐 안하냐 로 나누는 거 같은데
    주어지는 갯수대로 ch 만들고,
    예 6 개이면 6개로 뻗는다.
    
    '''
    DFS(1)

    return answer

N = 6
ch = [0] * N

inp = [1, 3, 5, 6, 7, 10]

re = solution()
print(re)
#=>
print('====================')


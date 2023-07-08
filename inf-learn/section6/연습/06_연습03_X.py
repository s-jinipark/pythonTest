
##### 부분집합 구하기(DFS)

def DFS(v):
    if v == N+1 :  # 종착점
        for i in range(1, N+1):
            if ch[i] == 1 :
                print(i, end=' ')
        print()
    else:
        ch[v]=1
        DFS(v+1)
        ch[v]=0
        DFS(v+1)

def solution():
    answer = 0
    '''
    상태 트리를 그려서 사용하냐 안하냐 로 나누는 거 같은데
    구현은 기억이 안남. 
    
    풀이 보고 함 .. =>
    2 * 2 * 2 = 8 가지 case 나오는데 공집합은 제거
    
    DFS 는 상태 트리 잘 그려야..
    DFS(v, use) 해서 구분하려 했는데 , 잘 안 됨
    
    '''
    DFS(1)

    return answer

N = 3
ch = [0] * (N+1)

re = solution()
print(re)
#=>
print('====================')


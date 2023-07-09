
##### 합이 같은 부분집합(DFS : 아마존 인터뷰)

def DFS(L,sum):
    global  yn
    if yn == 'YES':
        return
    if L == N :  # 종착지점. 0부터 시작했으므로...
        # 여기서 출력
        print(tot, sum , tot-sum)
        if sum == tot-sum :
            yn ='YES'
            print('YES')
            return
            #sys.exit(0)
    else :
        DFS(L+1, sum+inp[L])
        DFS(L+1, sum)

def solution():
    answer = 0
    '''
    마찬가지로 상태 트리를 그려서 사용하냐 안하냐 로 나누는 거 같은데
    주어지는 갯수대로 ch 만들고,
    예 6 개이면 6개로 뻗는다.
    
    [!] 아니었다!
    6개로 뻗는게 아니고,
    레벨을 6번 가고, 사용하냐 안 하냐 로 뻗는다
    뻗으면서 sum 을 누적
    
    '''
    #tot = sum(inp)  # 전역으로 이동
    print(tot)
    DFS(0, 0)

    return answer

N = 6

inp = [1, 3, 5, 6, 7, 10]
tot = sum(inp)
yn = ''

re = solution()
print(re)
#=>
print('====================')


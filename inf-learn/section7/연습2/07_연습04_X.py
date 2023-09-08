
##### 동전 바꿔주기(DFS)
def DFS(L, sum):
    #[2]
    if sum > T:
        return
    #<- [2]
    
    if L == K :  # 말단 노드
        if sum == T:
            print(sum)
    else :
        d, cnt = inp[L]
        #print(d, cnt)
        #for i in range(cnt):
        # [2] cnt + 1 안해서.. ㅠ.ㅠ.
        for i in range(cnt+1):
            DFS(L+1, sum + (d * i) )

def solution():
    answer = 0

    '''
    설명 듣고 다시...
    상태 트리
    동전 종류가 L 이고
    동전의 수만큼 가지를 뻗는다
    
    원문제는 동전 갯수가 100개 인데
    DFS 용으로 10개로 줄여서 했다는 ...
     
    '''

    DFS(0, 0)

    return answer

T = 20  # 지폐의 금액
K = 3   # 동전의 가지수

inp = [
    (5,3),
    (10,2),
    (1,5)
]

re = solution()
print(re)
#=>
print('====================')


##### 동전 분배하기(DFS)
def DFS(L):
    global  res
    if L == N :
        print(max(ch), min(ch), max(ch)-min(ch))
        cha = max(ch)-min(ch)
        # [2] 여기서 (조건) 단 세 사람의 총액은 서로 달라야 합니다.
        if res > cha:
            tmp = set()
            for i in ch:
                tmp.add(i)
            if len( tmp ) == 3:
                res = cha
    else :
        for i in range(3):
            ch[i] += inp[L]
            DFS(L+1)
            ch[i] -= inp[L]
            # 아래 처음 시도 ch[i] 에 넣었다 -> DFS하고 -> 빼야 되는데..
            # 뭔가 반대로 한거 같음.. DFS -> 넣었다 -> DFS
            # DFS( L+1, ch[i] )
            # ch[i] += inp[L]
            # DFS( L+1, ch[i] )

def solution():
    answer = 0

    '''
    상태 트리
    3명은 정해졌고,
    동전 N 개 가 L 
    가지는 3가지로
    '''

    DFS(0)
    print('res', res)
    return answer

N = 7   # 동전의 개수

inp = [8,9,11,12,23,15,17]
ch = [0] * 3

res = 2147000000

re = solution()
print(re)
#=>
print('====================')

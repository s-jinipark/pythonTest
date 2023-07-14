
##### 동전 바꿔주기(DFS)
def DFS(L, sum):
    if L == Max :
        if sum == T :
            print(sum)
    else :
        for i in range(K):
            if inp[i][1] > 0 :
                inp[i][1] -= 1
                DFS(L+1, sum + inp[i][0])
                inp[i][1] += 1
            else :
                DFS(L+1, sum )

def solution():
    answer = 0

    '''
    상태 트리
    지금 생각나는 건
    동전 중 max 인 갯수 만큼 L 진행
    가지는 동전 종류만큼 뻗는다. 갯수를 -1 해주어 0 이 되면 뻗지 않는다
    
    '''

    DFS(0, 0)
    # print(ch)
    # cnt = 0
    # for i in range(1, len(ch)):
    #     if ch[i] == 0:
    #         cnt += 1
    # print('cnt', cnt)
    return answer

T = 20  # 지폐의 금액
K = 3   # 동전의 가지수

inp = [
    [5,3],
    [10,2],
    [1,5]
]
# 동전 중 max
Max = 0
for i in inp:
    print(i)
    d, cnt = i
    if cnt > Max:
        Max = cnt
print(Max)

re = solution()
print(re)
#=>
print('====================')

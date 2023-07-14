
##### 양팔저울(DFS)
def DFS(L, sum):
    if L == K :
        print(sum)
        #if sum > 0 :
        # [2] 여기 강의 듣고 수정
        if 0 < sum <= tot :  # -1 하는 이유는 대칭적으로 나타나므로...
            ch[sum] = 1   # [2] set 을 사용해서 중복 제거...
    else :
        DFS(L + 1, sum + inp[L])   # 왼쪽에 놓는다
        DFS(L + 1, sum - inp[L])   # 오른쪽에 놓은다
        DFS(L + 1, sum )    # 무게를 재는데 사용하지 않겠다

def solution():
    answer = 0

    '''
    상태 트리
    강의 듣고 , L -> 1, 5, 7 로 나가고
    가지는 왼쪽에 놓는 경우(+), 오른쪽에 놓는 경우(-), 사용 안하는 경우
    (3가지로 뻗는다!!)
    
    '''

    DFS(0, 0)
    print(ch)
    cnt = 0
    for i in range(1, len(ch)):
        if ch[i] == 0:
            cnt += 1
    print('cnt', cnt)
    return answer

K = 3   # 개수

inp = [1,5,7]

tot = sum(inp)
ch = [0] * (tot+1)  # tot+1 해서 1 부터 사용 예정

re = solution()
print(re)
#=>
print('====================')

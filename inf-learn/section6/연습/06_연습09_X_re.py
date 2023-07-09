
##### 조합 구하기
'''
굉장히 중요하다며 강조...
'''
def DFS(L, S):

    if L == M : # 종착지점
        print(res)

    else:
        for i in range(S, N+1):
            res[L] = i
            #DFS(L+1, S+i)  # 내가 한거.. 값은 똑같이 나오는데.. 흠
            DFS(L+1, i+1)  # 강사도 S+1 로 헷갈려 함
def solution():
    answer = 0
    '''
    '''

    DFS(0,1)

    return answer

N = 4  # 구슬의 갯수

M = 2  # 뽑는 갯수

res = [0] * M

re = solution()
print(re)
#=>
print('====================')


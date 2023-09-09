
##### 조합 구하기
'''
굉장히 중요하다며 강조...
'''
def DFS(L, s):
    if L == M :
        print(res)
        return
    else :
        for i in range(s, N+1) :
            # if i in res :
            #     continue
            res[L]= i
            #DFS(L+1, s+1)  # s+1 아니래.. 강사도 헷갈림
            DFS(L+1, i+1)  # ★ ★

def solution():
    answer = 0
    '''
    '''

    DFS(0,1)  # 시작점을 지정해 줌

    return answer

N = 4  # 구슬의 갯수

M = 2  # 뽑는 갯수

res = [0] * M
ch = [0] * (N +1)  # 번호로 체크

re = solution()
print(re)
#=>
print('====================')


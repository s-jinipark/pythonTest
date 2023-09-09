
##### 조합 구하기
'''
굉장히 중요하다며 강조...
'''
def DFS(L):
    if L==M :
        print(res)
        return
    else:
        for i in range(1, N+1):
            if i in res:  # 이것도 필요
                continue
            if ch[i] == 0:
                ch[i] = 1
                res[L] = i
                DFS(L+1)
                ch[i] = 0

        # for i in range(1, N+1) :
        #     if i in res :
        #         continue
        #     res[L] = i
        #     DFS(L+1)
        # 이렇게 하면 [1,2] 와 [2,1] 이 같이 나옴
        # 조합이라서 이것도 같이

def solution():
    answer = 0
    '''
    '''

    DFS(0)

    return answer

N = 4  # 구슬의 갯수

M = 2  # 뽑는 갯수

res = [0] * M
ch = [0] * (N +1)  # 번호로 체크

re = solution()
print(re)
#=>
print('====================')


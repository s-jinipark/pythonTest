
##### 순열 구하기

def DFS(L):
    if L == M:
        print(res)
    else :
        for i in range(1,N+1):
            if i not in res:
                res[L] = i
                DFS(L+1)

def solution():
    answer = 0
    '''
    1부터 N까지 번호가 적힌 구슬이 있습니다. 이 중 M개를 뽑아 일렬로 나열하는 방법을 모두 출력
    
    2개 뽑는거니까 Level 2 까지.
    구슬 3개니까 3가닥으로 뻗어...
    
    '''

    DFS(0)

    return answer

N = 3  # 구슬의 갯수

M = 2  # 뽑는 갯수
res = [0] * M
sum = 0
min_val = 2147000000

re = solution()
print(re)
#=>
print('====================')


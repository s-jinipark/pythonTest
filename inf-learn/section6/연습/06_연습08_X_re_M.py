
##### 순열 구하기

def DFS(L):
    if L == M:  # 종착점
        print(res)
    else :
        for i in range(1,N+1):  # 가지 뻗는다
            #res[L] = i+1    # 난 여기 썻는데, 강의 보고 아래로 내림 (인덱스도 조금 헷갈려함)
            if ch[i] == 0:  # 적용 안된 경우
                ch[i] = 1
                res[L] = i
                DFS(L+1)
                ch[i] = 0

def solution():
    answer = 0
    '''
    1부터 N까지 번호가 적힌 구슬이 있습니다. 이 중 M개를 뽑아 일렬로 나열하는 방법을 모두 출력
    
    2개 뽑는거니까 Level 2 까지.
    구슬 3개니까 3가닥으로 뻗어...
    
    [2] 여기서 방문했던 것 체크
    '''

    DFS(0)

    return answer

N = 3  # 구슬의 갯수

M = 2  # 뽑는 갯수
res = [0] * M
sum = 0
min_val = 2147000000

ch = [0] * (N+1)

re = solution()
print(re)
#=>
print('====================')


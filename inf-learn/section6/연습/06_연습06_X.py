
##### 중복순열 구하기

def DFS(L):
    if L == M :  # 종료 지점
        print(res)
    else:
        for i in range(1, N+1):
            res[L]=i
            DFS(L+1)

def solution():
    answer = 0
    '''
    1부터 N까지 적힌 구슬..중복을 허락하여 M번 뽑아 일렬로 나열하는 방법 모두 출력
    M 번 레벨까지 가고 가지를 N번(1부터 N 번까지) 뻗으면 될 듯
    
    구현 방법이 생각이 안 나서.. 해설 듣고 진행
    
    '''
    DFS(0)

    return answer

N = 3  # 구슬 1부터 3
M = 2  # M번 뽑는다
res = [0] * M  # 뽑은 구슬 번호 저장

re = solution()
print(re)
#=>
print('====================')


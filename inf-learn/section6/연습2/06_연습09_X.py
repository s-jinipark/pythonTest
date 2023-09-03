
##### 수열 추측하기
def DFS(L):
    if sum(res) >
    if L == N :
        print(res, sum(res))
        return
    else:
        for i in range(1, 11): # 문제에 1부터 10 이라며
            res[L] = i
            DFS(L+1)

def solution():
    answer = 0
    '''
    풀이 보고 해 봄 
    일단 4 16 이 들어오면 
    4가지 숫자로 만들 수 있는 조합.. 다 구함
    더해서 16 인 것
    더할때 규칙이 있다 => 이항계수 라며...
    
    [얘는 일단. pass]
    '''

    DFS(0)

    return answer

N = 4  # N은 가장 윗줄에 있는 숫자의 개수를

F = 16  # F는 가장 밑에 줄에 있는 수
res = [0] * N
temp = [1,2,2,1]

re = solution()
print(re)
#=>
print('====================')



##### 알파코드(DFS)

def DFS(v):
    if v == len(inp):
        print(res)
    else :
        DFS(v+1)
        DFS(v+2)

def solution():
    answer = 0

    '''
    상태 트리
    입력값을 1자리와 2자리 경우로 나눠서...
    start 지점을 넘겨야 
    '''

    DFS(0)
    print('res', res)
    return answer


inp = '25114'
res = []

re = solution()
print(re)
#=>
print('====================')

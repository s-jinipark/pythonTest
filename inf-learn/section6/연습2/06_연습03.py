
##### 부분집합 구하기(DFS)
def DFS(v):
    if v == N+1 :
        #print(ch)
        if max(ch) == 0:
            return
        for i in range(1, N+1):
            if ch[i] == 1:
                print(i, end=' ')
        print()
        return
    else:
        #print(v)
        if ch[v] == 0:
            ch[v] = 1  # [2] 여기서 사용, 사용 안함을 chk 함
            DFS(v+1)
            ch[v] = 0
            DFS(v+1)

def solution():
    answer = 0

    DFS(1)  # 문제에 1 부터 N까지 라고
    # [2] 여기 0 부터 아닌가 고민했으나.
    
    return answer

N = 3
ch = [0] * (N+1)

re = solution()
print(re)
#=>
print('====================')


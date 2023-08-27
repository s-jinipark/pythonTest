
##### 이진트리 순회(깊이우선탐색)

def DFS(n):
    if n > L :
        return
    else:
        #print(n, end= ' ')  # 전위
        DFS(n*2)
        #print(n, end= ' ')  # 중위
        DFS(n*2 + 1)
        print(n, end= ' ')  # 후위

def solution():

    answer = 0
    DFS(1)  # 1부터 시작
    print()

    return answer

L = 7

re = solution()
print(re)
#=>
print('====================')


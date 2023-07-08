
##### 이진트리 순회(깊이우선탐색)

def DFS(x):
    if x > 7:  # 종료 조건
        return
    else :
        #print(x, end=' ')    # 전위 순회  => 1 2 4 5 3 6 7
        DFS(x*2)
        #print(x, end=' ')    # 중위 순회  => 4 2 5 1 6 3 7
        DFS(x * 2 +1)
        print(x, end=' ')    # 후위 순회  => 4 5 2 6 7 3 1

def solution():

    answer = 0
    DFS(1)
    print()

    return answer
'''
하나도 기억 안나서
풀이 보고 ... 해 봄
'''
#N = 7

re = solution()
print(re)
#=>
print('====================')


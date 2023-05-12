
graph = [
    [],             # tmp5-x_그래프... (그림 참조)
    [2, 3, 8],      # 노드 1에 연결된 노드들
    [1, 7],         # 노드 2에 연결된 노드들 ...
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

def dfs(x) :
    #print(visited)
    visited[x] = True  # 방문 표시
    print(x, end=' ')
    for i in graph[x] :
        #print(i, end=' ')
        if not visited[i] :
            dfs(i)
    #print()

dfs(1) # 1 부터 시작 , graph 에 0 은 없당.
#print(visited)  # 마지막 찍어 보면 0 제외하고 True 설정

print()
print("------------------------------")
visited = [False] * 9

def bfs(x) :
    #print(visited)
    #visited[x] = True  # 방문 표시
    #print(x, end=' ')
    qu = []
    qu.append(x)
    while len(qu) > 0 :
        tmp = qu.pop(0)
        #print(tmp)
        for i in graph[tmp]:  # 큐에서 뽑은 tmp 활용 -> graph[tmp]
            if not visited[i] :
                qu.append(i)
                visited[i] = True
                print(i, end=' ')
    #print()

bfs(1) # 1 부터 시작 , graph 에 0 은 없당.
#print(visited)  # 마지막 찍어 보면 0 제외하고 True 설정


# 연습용 ----------------------------------------
# def factorial(n):
#     if n <= 1 :
#         return 1
#     return n * factorial(n-1)
#
# res = factorial(5)
# print(res)

# def factorial(n) :
#     print(n)
#     # 끝나는 조건
#     if n <= 1 :
#         return 1
#     # else :
#     #     print(n , '+', n-1)
#     #     return n + factorial(n-1)
#     # 걍 리턴
#     return n + factorial(n-1)
#
# print(factorial(5))
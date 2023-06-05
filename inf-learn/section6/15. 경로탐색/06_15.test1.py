
def DFS(v):
    global cnt
    if v == n :
        cnt += 1
        print(path)
        #return
    else :
        for i in range(1, n+1):  # 1 번 부터 돌아야...
            if g[v][i] == 1 and ch[i] == 0 :
                ch[i] = 1
                path.append(i)
                DFS(i)
                ch[i] = 0 # 다시 풀어주어야.(*)
                path.pop()  # 넣었던거 빼준다

def solution():
    answer = 0
    #path =[]   # path 를 찍어 봄
    path.append(1)  # 기본으로 넣어주어야

    ch[1] =1
    DFS(1)  # 1 부터

    print(cnt)
    return answer

n = 5   # 정점의 수
k = 9   # 간선의 수
inp = [(1,2),(1,3),(1,4),(2,1),(2,3),
       (2,5),(3,4),(4,2),(4,5)]

g = [[0]*(n+1) for _ in range(n+1)]  # 숫자 그대로 넣기위해 +1
ch = [0]*(n+1)
cnt = 0

for i in inp:
    g[i[0]][i[1]] = 1

print(g)
path = []  # path 를 찍어 봄
re = solution()

print('re :', re)
#=>
print('==============================')

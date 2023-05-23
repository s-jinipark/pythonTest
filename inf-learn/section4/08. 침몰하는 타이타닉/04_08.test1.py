
# 프로그래머스 스타일 로 ...
def solution(N, M, inp):
    answer = 0

    inp.sort()
    print(inp)

    visited = [False] * N
    print(visited)

    for i in range(len(inp)):
        for j in range(len(inp)-1, -1, -1):
            print(i, j)
            if i + j <= M  and visited[i] == False and visited[j] == False:
                answer +=1
                visited[i] = True
                visited[j] = True
                break

    return answer

N = 5
M = 140   # 몸무게

inp = [90, 50, 70, 100, 60]

re = solution(N, M, inp)
print('re :', re)
#=>
print('==============================')



# 비슷하게 생각은 남

def DFS(v, sum):
    global cnt
    if sum>T:
        return

    if v == k :
        if sum == T:
            print(sum)
            cnt += 1
            return
    else:
        for i in range(inp[v][1]+1) : # 개수 (안쓰는거 포함 0, 1, .., max 포함 위해 +1 해줌)
            print(i)
            DFS(v+1, sum+(inp[v][0] * i))

    ##### 1st
    # if v >= k :
    #     return
    # if sum == T:
    #     print(sum)
    #     return
    # else:
    #     for kk in range(k):   # 첫 번째 시도 이부분이 잘 안됨
    #         for i in range(1, inp[v][1]+1):
    #             #print(i)
    #             DFS(v+1, sum+((inp[v][0])*i))

def solution():
    answer = 0

    DFS(0,0)  # Lvl : 동전의 종류, sum : 액수
    print('cnt:', cnt)
    return answer

T = 20   # 지폐의 금액
k = 3    # 동전의 가지수
inp = [(5,3),(10,2),(1,5)]   # 금액과 개수
cnt = 0

re = solution()
print('re :', re)
#=>
print('==============================')

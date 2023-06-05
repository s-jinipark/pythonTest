
def DFS(v, sum):
    global  maxVal
    if v == N:
        print(sum)
        if maxVal < sum:
            maxVal = sum
        return
    else :
        DFS(v+inp[v][0], sum+inp[v][1])
        if v+1 < N:
            DFS(v+ inp[v+1][0], sum+ inp[v+1][1])

def solution(N):
    answer = 0

    DFS(0,0)  # Lvl : 일(1일, 2일), sum : 금액
    print('maxVal:', maxVal)
    return answer

N = 7   # N+1 휴가 감, 상담할 수 있는 일

inp = [(4,20),(2,10),(3,15),(3,20),(2,30),(2,20),(1,10)]
maxVal = 0

re = solution(N)
print('re :', re)
#=>
print('==============================')

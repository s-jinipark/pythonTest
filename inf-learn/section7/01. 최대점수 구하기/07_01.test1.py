
def DFS(v, sum, time):
    global  maxVal

    if time > M :  # 제한시간 cutting
        return

    if v == N :
        if maxVal < sum:
            maxVal = sum
        print(sum)
    else :
        DFS(v+1, sum+inp[v][0], time+inp[v][1])
        DFS(v+1, sum, time)

def solution(N):
    answer = 0

    DFS(0,0,0)  # Lvl : 문제, sum : 점수, time : 시간
    print('maxVal:', maxVal)
    return answer

N = 5   # 문제의 개수
M = 20  # 제한 시간
inp = [(10,5),(25,12),(15,8),(6,3),(7,4)]
maxVal = 0

re = solution(N)
print('re :', re)
#=>
print('==============================')

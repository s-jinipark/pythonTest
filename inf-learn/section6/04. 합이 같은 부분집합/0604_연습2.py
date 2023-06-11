
# 풀이 본 후
def DFS(v, sum):
    global  rtn
    if v ==N :  # 종료 조건
        print(sum)
        total = 0
        for i in inp:
            total += i
        if sum == total-sum :
            rtn = 'YES'
        return
    else:
        DFS(v+1, sum + inp[v])    # 넣느냐
        DFS(v+1, sum)   # 그냥 가느냐

def solution(N):
    answer = 0

    DFS(0, 0)  # 인자 두개고, sum 을 넘김

    return answer


N = 6
inp = [1,3,5,6,7,10]
#rtn = ''

rtn = 'NO'

re = solution(N)
print('re :', re)

print(rtn)


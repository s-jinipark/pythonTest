
def DFS(L, sum) :
    global maxVal
    if L == N :
        if sum > C :
            return
        print('sum', sum)
        if maxVal < sum :
            maxVal = sum
    else :
        DFS(L+1, sum + inp[L])  # sum 을 더한 것과 안 더한 것으로...
        DFS(L+1, sum )


def solution(C, N, inp):
    answer = '' #0

    DFS(0, 0)  # 이것도 level 하고 sum ??
    print(maxVal)
    return answer

C = 259
N = 5
inp = [81,58,42,33,61]
maxVal = 0

re = solution(C, N, inp)

print('re :', re)
#=>
print('==============================')

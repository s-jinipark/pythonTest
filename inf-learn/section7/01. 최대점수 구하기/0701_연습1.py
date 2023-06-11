
# 풀이보고 다시..
def DFS2(L, sum, time):
    global  maxVal
    if L == N : # 종료 조건
        if time <= M  and sum > maxVal:
            print('sum, time : ', sum, time)
            maxVal = sum

        return
    else:
        DFS2(L+1, sum+inp[L][0], time+inp[L][1])
        DFS2(L+1, sum, time)

def solution2():
    answer = 0

    DFS2(0, 0, 0)   # 점수, 시간을 넘기면서 계산

    return answer


# self
def DFS(L):
    global  res

    if L == N :  # 종료 조건
        print(chk)
        sum = 0
        tot_time = 0
        for i in range(N):
            if chk[i] == 1 :
                scor, time = inp[i]
                sum += scor
                tot_time += time
        print(sum, tot_time)
        #시간안에 얻을 수 있는 최대 점수
        if tot_time <= M and sum > res :  # 제한시간안에 들어오면서
            # 큰 수
            res = sum

        return
    else:
        # 2가지로 뻗는다
        chk[L] = 0
        DFS(L + 1)
        chk[L] = 1
        DFS(L + 1)

def solution():
    answer = 0
    # 문제를 풀 것인가, 아닌가 로 구분
    DFS(0)

    return answer

# 문제의 개수N(1<=N<=20)과 제한 시간 M(10<=M<=300)이 주어집니다.
N = 5
M = 20
inp = [
    [10, 5 ],
    [25, 12],
    [15, 8 ],
    [6 , 3 ],
    [7 , 4 ]
]

chk = [0] * N
res = 0

re = solution()
print('re :', re)

print('res :', res)

#==============================

maxVal = 0
re2 = solution2()
print('re2 :', re2)
print('maxVal :', maxVal)


# 시간 초과 남

def DFS(v,tot, cnt):
    global  maxCnt
    if v == len(apartments) :
        #print(v, tot)
        if tot <= money:
            print(v, tot, cnt)
            maxCnt = max(maxCnt, cnt)
        return
    else:
        if tot > money :
            return
        # 계산값
        tmp = apartments[v][0] - int( apartments[v][1]*(apartments[v][0]/100) )
        DFS(v+1, tot+tmp, cnt+1)
        DFS(v+1, tot, cnt)

def solution(apartments, money):
    answer = 0
    tot = 0
    cnt = 0
    #maxCnt = 0

    # DFS 가지치기 인데.. 기억이 안남
    # 계산 먼저 해봐야 함
    # for a in apartments:
    #     print(a[0], int( a[1]*(a[0]/100) ) )
    DFS(0, tot, cnt )
    print("maxCnt : ", maxCnt)
    return answer


apartments = [[100000, 70],[15000, 90],[20000, 50]]
money = 30000
maxCnt = 0

an = solution(apartments, money)
print(an)

# 상태 트리 그리는 게 핵심인데
# 동전의 갯수가 L 이고, 3명에게 제공한다는...(각각 DFS)

def DFS(L, res):
    global  minVal
    if L == N :
        tmp = max(res)- min(res)
        print(res, min(res), max(res), 'minus:', tmp)
        # 조건이 있음. 문제 잘 읽어야 함(1st 에 답이 다르게 나왔음)
        # [단 세 사람의 총액은 서로 달라야 합니다.]
        tmp_s = set()
        for r in res:
            tmp_s.add(r)

        #if minVal > tmp :  # 이거 아니고
        if minVal > tmp and len(tmp_s) == 3:
            minVal = tmp
        return
    else :
        for i in range (3):  # 가지가 뻗어 나가는 ... 문제에서 3명으로 정해져 있으므로..
            res[i] += inp[L]
            DFS(L+1, res)  # 다음 동전으로
            res[i] -= inp[L]  # 중요! - Back 한 상황이므로

def solution():
    answer = 0

    res = [0]* 3  # 문제에 3명에게 나눠 준다고 ...
    DFS(0, res)  # Lvl : 동전의 종류
    print('minVal:', minVal)
    return answer

N = 7   # 동전의 개수

inp = [8,9,11,12,23,15,17]   # 금액
cnt = 0
minVal= 2147000000
re = solution()
print('re :', re)
#=>
print('==============================')

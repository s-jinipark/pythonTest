
# self
def DFS(L):
    global res
    if L == N :  # 말단 노드
        print(money)
        cha = max(money) - min(money)
        if cha < res :
            # 3개의 값이 달라야 한다
            tmp = set()
            for x in money:
                tmp.add(x)
            if len(tmp) == 3:
                res = cha
        return
    else:
        # 3갈래로 뻗는다
        for i in range(3):
            money[i] += inp[L]
            DFS(L+1)
            money[i] -= inp[L]

def solution():
    answer = 0

    DFS(0)

    return answer

#  동전의 개수 N(3<=N<=12)
N = 7

# 동전의금액
inp = [ 8,9,11,12,23,15,17 ]
money = [0] * 3
res = 214700000

re = solution()
print('re :', re)
print('res :', res)
'''
3 명 에게 나누어 준다 했으니
L : 3, 가지수는 7 가지

=> 풀이 봤더니
L : 동전,  가지수가 3가지 라는
money[0, 0, 0] 으로 만들어서,
A, B, C 사람별로 sum
[완전 반대로 했음..ㅠ.ㅠ]

'''

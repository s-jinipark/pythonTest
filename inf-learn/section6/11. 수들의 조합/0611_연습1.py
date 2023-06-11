
# self
# 풀이 봄 (중요하다고 강조)
#def DFS(L, s):
# [2] sum 까지 추가
def DFS(L, s, sum):

    global  res

    if L == K :  # 종료조건
        print(res)
        if sum % M == 0 :
            print('>', res)
        return
    else :
        for i in range(s, N):  # s 부터 뻗는다. N 까지라는 점(**)
            res[L] = inp[i]  # 여기.. 중요  **
            #DFS(L + 1, i + 1)
            # [2]
            DFS(L + 1, i + 1, sum + inp[i])

def solution(N):
    answer = 0

    #DFS(0, 0)   # 인자가 하나 더 있음 s (start) , 여기가 0, 0 이라는 점
    # [2] sum 까지 넣자
    DFS(0, 0, 0)

    return answer

# N개의 정수가 주어지면 그 숫자들 중 K개를 뽑는 조합의 합이
N = 5
K = 3
inp = [2, 4, 5, 8, 12]
# 수 M의 배수인 개수는 몇 개가 있는지 출력
M = 6
#rtn = ''
res = [0] * K

re = solution(N)
print('re :', re)


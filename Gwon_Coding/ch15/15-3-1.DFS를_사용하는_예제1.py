
import sys
'''
N개의 정수로 이루어진 수열이 있을 때, 
크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이
S 가 되는 경우의 수를 구하는 프로그램을 작성하시오

'''
def dfs(idx, sum):
    global answer
    if (idx >= N):
        return
    sum += lst[idx]
    if (S==sum):
        answer += 1
    dfs(idx+1, sum-lst[idx])  # 둘다 다음으로 이동인데
    dfs(idx+1, sum )          # 현재 정점의 수열을 택하지 않냐, 택하냐

inp1 = '5 0'
inp2 = '-7 -3 -2 5 8'
N, S = map(int, inp1.split())
lst = list(map(int, inp2.split()))
print(N, S, lst)

answer = 0
dfs(0,0)
print(answer)

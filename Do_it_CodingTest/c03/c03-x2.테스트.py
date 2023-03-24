import sys

def print_grace(lst) :
    for l in lst:
        print(l)

sys.stdin = open("input_c03-x2.txt", "rt")

n, m = map(int, input().split())
print(n, m)  # 리스트 수 , 질의 수

A = [[0]*(n+1)]  # 얘는 워지 ? 1차원에서 맨앞에 0 놨던...
print(A)

D = [[0]*(n+1) for _ in range(n+1)]
print('---------------')
print_grace(D)


for i in range(n):
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)

print('---------------')
print_grace(A)

for i in range(1, n+1):
    for j in range(1, n+1) :
        # 합 배열 구하기
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]

print('---------------')
print_grace(D)

for _ in range(m) :   # 질의
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[x2][y1-1] - D[x1-1][y2] + D[x1-1][y1-1]
    print(result)

print('--------------------')
print('연속된 자연 수의 합')

'''
정수 N 이 주어지고
이 수를 연속된 자연수의 합으로 나타내는 가지 수
'''

N = 15

start_idx = 1
end_idx = 1
cnt = 1  # 해당 수 -> 미리 반영
sum = 1

while end_idx != N :
    if sum == N :
        cnt += 1
        end_idx += 1
        sum += end_idx   # <-* 증가
    elif sum >  N :  # N 보다 크다면
        sum -= start_idx  # sum 을 줄여야 하니까..
        start_idx += 1
    else :
        end_idx += 1  # idx 증가, sum 증가 순서를 맞춰 주어야 함.
        sum += end_idx

print(cnt)


print('--------------------')
print('주몽의 명령 - (응용) 연속된 자연 수의 합')

'''
재료의 개수 N
갑옷이 완성되는 번호의 합 M [ => 재료 중 2 개 더해서 M 을 만들면 됨]
'''
N = 6
M = 9
inp = '2 7 4 1 5 3'

lst = list(map(int, inp.split()))
print(lst)
lst.sort()
print(lst)

start_idx = 0
end_idx = N-1
cnt = 0

while start_idx < end_idx :
    if lst[start_idx] + lst[end_idx] < M :
        start_idx += 1
    elif lst[start_idx] + lst[end_idx] > M :
        end_idx -= 1
    else :
        cnt += 1
        print('>', lst[start_idx] , lst[end_idx] )
        start_idx += 1
        end_idx -= 1    # 동시에 앞, 뒤로 ...

print(cnt)


print('--------------------')
print('좋은 수 구하기 - 투 포인터')

'''
자기 자신을 좋은 수 만들기에 포함하면 안 됨 
'''
N = 10
inp = '1 2 3 4 5 6 7 8 9 10'

A = list(map(int, inp.split()))
A.sort()
print(A)
result = 0

for k in range(N):
    find = A[k]
    i = 0
    j = N-1  # ? 맨 뒤 라고 ?
    while i < j :
        if A[i] + A[j] == find :
            print(find, ' - ', A[i] , A[j])
            if i != k and j != k :  # 이 부분 꼭 필요 ??
                result += 1
                break
            elif i == k :
                i += 1
            elif j == k :
                j -= 1
        elif A[i] + A[j] < find :
            i += 1
        else :
            j -= 1

print(result)

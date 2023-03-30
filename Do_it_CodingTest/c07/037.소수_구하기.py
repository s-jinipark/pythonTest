
import math

inp = '3 6'

'''
1번째 줄에 자연수 M 과 N 이 주어짐

'''
M, N = map(int, inp.split())
print( M, N )

A = [0] * (N+1)  # 하나 더 많게 ? [인덱스랑 숫자랑 맞추는 ...]

for i in range(2, N+1):
    A[i] = i

print(A)

for i in range(2, int(math.sqrt(N)) + 1):  # 제곱근까지만 수행
    print(i, math.sqrt(N))
    if A[i] == 0 :
        continue
    for j in range(i+i, N+i, i) :  # 배수 지우기
        A[j] = 0
print(A)
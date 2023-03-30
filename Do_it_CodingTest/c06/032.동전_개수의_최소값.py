
import sys

sys.stdin = open("input_032.txt", "rt")

N, K = map(int, input().split())

A = [0] * N

for i in range(N):
    A[i] = int(input())

print(N, K)
print(A)

count = 0

for i in range(N-1, -1, -1) :  # [뒤 부터 오는게 이거임]
    #print(A[i])
    #print(int(K/A[i]))
    if A[i] <= K :  # 현재 동전의 가치가 K 보다 작거나 같으면 구성에 추가
        count += int(K/A[i])
        print(K/A[i], int(K/A[i]), K % A[i])
        K = K % A[i]  # K 를 현재 동전을 사용하고 남은 금액으로 갱신

print(count)

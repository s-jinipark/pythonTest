import sys
sys.stdin = open("input.txt", "rt")  # 채점 전 주석 처리
n, k = map(int, input().split()) # N의 약수들 중 K번째로 작은 수를 출력

# yaksu = []
# for i in range(1,n+1) :
#     print(i)
#     if n % i == 0 :
#         yaksu.append(i)
# print(yaksu)
# yaksu.sort()
# print(yaksu[k-1])   # 0 부터 이므로 -1 수행

# 어차피 순서대로 수행
cnt = 0
for i in range(1, n+1) :
    if n % i == 0 :
        cnt += 1
    if cnt == k :
        print(i)
        break
else :
    print(-1)
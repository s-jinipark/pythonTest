
import sys

sys.stdin = open("input_c05-029.txt", "rt")

N = int(input())
A = list(map(int, input().split()))
print(N, A)
A.sort()

M = int(input())
tgt_lst = list(map(int, input().split()))


for i in range(M):
    find = False
    tgt = tgt_lst[i]
    # 이진 탐색 시작
    start = 0
    end = len(A) -1
    while start <= end :
        midi = int((start+end)/2)
        midv = A[midi]
        if midv > tgt :
            end = midi -1
        elif midv < tgt :
            start = midi +1
        else :
            find = True
            break
    if find :
        print(1)
    else:
        print(0)



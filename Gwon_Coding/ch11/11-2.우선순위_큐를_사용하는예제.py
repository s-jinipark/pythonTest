
# 일단, 책 참조 해서.

import sys
import heapq

sys.stdin = open("input11-2.txt", "rt")
n = int(input())
heap = []

for _ in range(n):
    num = int(input())
    #print(num)
    if num != 0 :  # 자연수라면, 우선순위 큐에 데이터 추가
        heapq.heappush(heap, (-num))  # 최소 힙을 기반으로 구현되어 있으므로 -num
    else:                             # =>  가장 낮은 값을 힙의 루트에 위치
        try:
            print(-1 * heapq.heappop(heap))  # 가장 큰 값을 출력하고 우선 순위 큐에서 삭제
        except:                              # =>  heapq.heappop() 형식 이용 (-1 곱하여 출력)
            print(0)
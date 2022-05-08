import sys
sys.stdin = open("input.txt", "rt")  # 채점 전 주석 처리

# N장의 카드를 가지고 있습니다. 같은 숫자의 카드가 여러장 있을 수 있음
# K번째로 큰 수 (3장 뽑는 것으로)
n, k = map(int, input().split())
a = list(map(int, input().split()))

# set 이라는 자료구조는 반복 제거
res = set()



'''
한 개의 회의실 , 이를 사용하고자 한는 N개의 회의

회의가 겹치지 않게 하면서 , 회의실을 사용할 수 있는 회의의 최대 개수

[문제 봤을 때 ..]
가장 빠른 시간 & 짧은 거 찾으면 될 듯
?

[책 잠깐 읽어 보면]
 1) 회의가 끝나는 시간이 빠를 수록 더 많은 회의를 고를 수 있다
 2) 끝난 시간 이후부터 가장 빨리 시작되는 회의를 골라야 한다

'''

import sys

sys.stdin = open("input12-3.txt", "rt")
N = int(input())
meet = []

for i in range(N):
    A, B = map(int, input().split())
    meet.append([A, B])

print(meet)
meet.sort(key=lambda x: (x[1], x[0]))
# 회의가 끝나는 시간이 빠른 순으로,
# 끝나는 시간이 같다면 회의 시작 시간이 빠른 순으로 리스트를 정렬
print(meet)

answer = 0
endTime = 0

for i in range(len(meet)) :
    if endTime <= meet[i][0] :
        endTime = meet[i][1]
        answer += 1

print(answer)


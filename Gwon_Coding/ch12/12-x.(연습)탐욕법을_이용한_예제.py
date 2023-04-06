
# 괄호를 적절히 쳐서 최소로 만드는 ..

#inp1 = '55-50+40'
#inp1 = '10+20+30+40'
inp1 = '00009-00009'

'''
마이너스 로 먼저 나눈 뒤
안에 + 있는 것 처리.
'''

minus = list(inp1.split('-'))
print(minus)

amt = 0
for i in range(len(minus)):
    m = minus[i]
    if m.find('+') :
        tmp = list(map(int, m.split('+')))
        tmp_amt = 0
        for t in tmp:
            tmp_amt += t
    if i == 0 :
        amt = tmp_amt
    else :
        amt -= tmp_amt
print(amt)

print('--------------------')
'''
한 개의 회의실 있는데,
각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 최의의 최대 개수

'''
import sys

sys.stdin = open('input12-3.txt', 'rt')

N = int(input())
print(N)
meet = []

for i in range(N):
    A, B = map(int, input().split())
    meet.append([A,B])

print(meet)

meet.sort(key=lambda x: (x[1], x[0]))
#-> 회의가 끝나는 시간 의 작은 값이 앞에 오게 오름차순으로 정렬
print(meet)

answer = 0
endTime = 0

for i in range(len(meet)) :
    if endTime <= meet[i][0] :   # 시작 시간
        endTime = meet[i][1]     # 끝나는 시간
        answer += 1

print(answer)

print('--------------------')
'''
크기가 N 인 배열 A -> 배열에 있는 모든 수는 서로 다르다
이 배열을 소트할 때, 연속된 두 개의 원소만 교환할 수 있다
소트한 결과가 사전 순으로 가장 뒷서는 것을 출력
'''

N = 7   # 크기
a_str = '10 20 30 40 50 60 70'
S = 1   # 교환 횟수

A = list(map(int, a_str.split()))
print(A)


# 6-1-1 ArrayList 를 사용하는 예제
# N 개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성
n = 5
inp = "20 10 35 30 7"

lst = list(map(int, inp.split()))
print(lst)

min_val = lst[0]
max_val = lst[0]

for i in range(1, n):
    if lst[i] < min_val :
        min_val = lst[i]
    elif lst[i] > max_val :
        max_val = lst[i]

print(min_val, max_val)

print('####################')

import sys

sys.stdin = open("input_6.1_2.txt", "rt")
'''
t_list = [[] for _ in range(5)]  # 일단 5개 만든다
r_list = [0 for _ in range(5)]
print(t_list, r_list)

for i in range(5):
    tmp_list = list(map(int, input().split()))
    print(tmp_list)
    t_list[i] = tmp_list
print(t_list)

top_sum = 0  # 최고 점수
top_no = 0  # 우승자 번호

# 넣으면서 해도 될 것 같지만
for i in range(5):
    tmp_sum = 0
    for j in t_list[i]:
        tmp_sum += j
    if tmp_sum > top_sum:
        top_sum = tmp_sum
        top_no = i +1
print(top_no, top_sum)
'''

# 여기서는 한번에 받는다
human=[list(map(int, input().split()) ) for _ in range(5)]

humanScore = [0] * 5

print(human, ' - ', humanScore)

score = 0  # 최대 점수 저장

for i in range(5):  # 5명이라고 조건이 주어짐
    sum = 0
    for j in range(4):  # 자신 빼고니까-> 4
        sum += human[i][j]
    humanScore[i] = sum
    score = max(score, sum)  # [괄호] 넣기에 이거 많이 나오는 듯

#print(score)
for i in range(5):
    if humanScore[i] == score :
        print(i+1, score)
        break

print('####################')

inp1 = '4 2'
inp2 = '1924'


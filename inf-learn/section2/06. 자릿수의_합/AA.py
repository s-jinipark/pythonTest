import sys


def digit_sum(x):
    tmp = 0
    for j in range(len(x)):
        tmp += int(x[j])
    #print('>', 연습)
    return tmp

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")


n = int(input())  # N 명
#n, k = map(int, input().split())
#a = list(map(int, input().split()))
# str 로
a = list(map(str, input().split()))
#print(a)
max_val = ''
max_sum = 0
# for i in a :
#     #print(i)
#     연습 = 0
#     for j in range(len(i)):
#         print(i[j])
#         연습 += int(i[j])
#     print(연습)
#     if 연습 > max_val :
#         max_val = 연습

# [2]
for i in a :
    #print(i)
    tmp = digit_sum(i)
    if tmp > max_sum :
        max_sum = tmp
        max_val = i
print(max_val)


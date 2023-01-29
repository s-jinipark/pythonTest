
# 문제 002 > 평균 구하기
#

'''
최대값을 고름
최대값을 M 이라고 할 때 모든 점수를 '점수/M *100' 으로 고침
-> 새로운 평균 ?
'''
#num = int(input())
#num = 3
num = 3
print(num)

#lst = list(map(int, input().split()))
#lst = [40, 80, 60]
lst = [10, 20, 30]
print(lst)

max_num = lst[0]
for i in range(1, num):
    if max_num < lst[i]:
        max_num = lst[i]

print(max_num)
sum = 0
for j in lst:
    sum = sum + j/max_num *100

print(sum/num)

'''
변환 점수의 평균을 구하는 식 

(A / M *100 + B / M *100 + C / M *100) /3
= (A + B + C) *100 / M / 3

'''
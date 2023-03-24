
# 숫자의 개수
# 공백없이 주어진 N 개의 숫자

N = 5
num = 54321
# -> int 는 list 로 변환도 안되고 하니...
# 스트링으로 바꾼뒤 list 로?
st_num = str(num)
lst = list(st_num)
print(lst)

sum = 0
for i in range(N):
    print(lst[i])
    sum += int(lst[i])

print('sum', sum)

print('--------------------')

in1 = 4 #3
in2 = '1 100 100 100' #'40 80 60'

lst = list(map(int, in2.split(' ')))
print(lst, max(lst))

max_val = max(lst)
for i in range(in1):
    lst[i] = lst[i]/max_val *100

print(lst)
sum = 0
avg = 0
for i in range(in1):
    sum += lst[i]

avg = sum/in1
print(avg)

'''
그런데..
(A/M*100 + B/M*100 + C/M*100) / 3 = (A+B+C)*100/M / 3
동일 하다는 사실
'''

print('--------------------')

in1, in2 = 5, 3  # 데이터의 갯수 , 질의(Q) 개수
in3 = '5 4 3 2 1'  # 구간 합을 구할 대상 배열
in4 =['1 3', '2 4', '5 5']

lst1 = list(map(int, in3.split()))
print(lst1)
lst2 = [0]*5
for i in range(in1) :
    if i > 0 :
        lst2[i] = lst1[i] + lst2[i-1]
    else :
        lst2[i] = lst1[i]
print(lst2)

for j in in4 :
    #print(j)
    tmp_lst = list(map(int, j.split(' ')))
    print(tmp_lst)
    if tmp_lst[0] == 1 :
        print(lst2[tmp_lst[1]-1])
    else :
        print(lst2[tmp_lst[1] - 1] - lst2[tmp_lst[0] -1 -1])
#=> 이상한 예외 케이스가 많을 것 같으나 일단...

print('--------------------')
print('책에 있는')
import sys

sys.stdin = open("input_c03-x1.txt", "rt")

suNo, quizNo = map(int, input().split())
numbers = list(map(int, input().split()))
#print(numbers)

prefix_sum = [0]
temp = 0

for i in numbers:
    temp = temp + i
    prefix_sum.append(temp)

print(prefix_sum)
# => [0, 5, 9, 12, 14, 15]  앗! index 를 고려해서 맨 앞에 0 넣어 둠..

for i in range(quizNo):
    s, e = map(int, input().split())
    print(prefix_sum[e] - prefix_sum[s-1])


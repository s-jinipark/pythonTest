
import sys

'''
자연수 N 과 M 이 주어졌을 때, 아래 조건을 만족하는 길이가 M 인 수열을 모두 구하는 프로그램
 ㆍ 1 부터 N 까지 자연수 중에서 중복 없이 M 개를 고른 수열

'''

#inp = '3 1'
inp = '4 2'
N, M = map(int, inp.split())
print(N, M)

# 이거 쓰면 되는 줄 알았는데
from itertools import permutations
# 1,1 같이 중복된 수 가 나오려면 product 써야
from itertools import product

tmp_list  =[]
for i in range(1,N+1):
    tmp_list.append(i)

tmp_list2 = list(permutations(tmp_list, M))
print(tmp_list2)
tmp_list3 = list(product(tmp_list, repeat=2))
print(tmp_list3)

print('----- 책 -----')
answer = []

def backt(depth):
    if depth == M :
        print(answer)
        return
    for i in range(1, N+1):
        if i in answer:  # 이 두 줄 넣어 주는 거 ..ㅠ
            continue
        answer.append(i)
        backt(depth+1)
        answer.pop()

backt(0)

'''
[참조]
https://juhee-maeng.tistory.com/91

'''

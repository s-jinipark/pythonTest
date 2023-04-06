
import sys

'''
자연수 N 과 M 이 주어졌을 때, 아래 조건을 만족하는 길이가 M 인 수열을 모두 구하는 프로그램
 ㆍ 1 부터 N 까지 자연수 중에서 M 개를 고른 수열
 ㆍ 같은 수를 여러번 골라도 된다
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

def backTracking(depth):
    if depth == M :
        print(' '.join(map(str, answer)))
        return
    for i in range(1, N+1):
        answer.append(i)
        backTracking(depth+1)  # [마지막까지 갔다가 아래 pop 되면서 다 빠짐]
        answer.pop()

backTracking(0)


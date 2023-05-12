
# N과 M (1)
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
#   . 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

from itertools import permutations
from itertools import combinations

#N, M = 3 , 1
N, M = 4 , 2
inlist = [1,2,3,4]
print(N, M)

res = []

res = list( permutations(inlist, 2) )
#print(res)
for r in res:
    print(r)
#====================

# N과 M (2)
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
#   . 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
#   . 고른 수열은 오름차순이어야 한다.
# => [2, 1], [3, 1] 같은 거 제외 하겠다는

print('--------------------')

res = []

res = list( combinations(inlist, 2) )

for r in res:
    print(r)

#====================

# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
#   . 1부터 N까지 자연수 중에서 M개를 고른 수열
#   . 같은 수를 여러 번 골라도 된다.
# => 이거는 아무 조건 없는  ..

print('--------------------')

# 중복 조합(=combinations_with_replacement)
# 출처: https://juhee-maeng.tistory.com/91 [simPLE:티스토리]

from itertools import product


res = []

for i in product(inlist, repeat=2):
    #print(i, end=" ")
    print(i)


#====================

# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
#   . 1부터 N까지 자연수 중에서 M개를 고른 수열
#   . 같은 수를 여러 번 골라도 된다.
#   . 고른 수열은 비내림차순이어야 한다.
#       .. 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.
# => 중복있는 오름차순.. 문제 설명이 더 어려움...

print('--------------------')

# 중복 조합(=combinations_with_replacement)
# 출처: https://juhee-maeng.tistory.com/91 [simPLE:티스토리]

from itertools import combinations_with_replacement


res = []

res = list( combinations_with_replacement(inlist, 2) )

for r in res:
    print(r)
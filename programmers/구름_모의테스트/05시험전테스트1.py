
# combinations(iterable, r) : iterable에서 원소 개수가 r개인 조합 뽑기
from itertools import combinations
#l = [1,2,3]
l = [3,2,1]
lst = list(combinations(l, 2))
print(lst)

# 결과 => [(3, 2), (3, 1), (2, 1)]
'''
파이썬 공식문서에 따르면 입력 iterable의 순서에 따라 사전식 순서로 방출됩니다. 
따라서, 입력 iterable이 정렬되어있으면, 조합 튜플이 정렬된 순서로 생성됩니다.
'''


# combinations_with_replacement(iterable,r) : iterable에서 원소 개수가 r개인 중복 조합 뽑기
from itertools import combinations_with_replacement

l2 = ['A', 'B', 'C']
lst2 = list(combinations_with_replacement(l2, 2))
print(lst2)

# 결과 => [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]


# permutations(iterable,r=None) : iterable에서 원소 개수가 r개인 순열 뽑기
from itertools import permutations

l3 = ['A','B','C']
lst3 = list(permutations(l3, 2))
lst3_2 = list(combinations(l3, 2))
print(lst3)
print(lst3_2)



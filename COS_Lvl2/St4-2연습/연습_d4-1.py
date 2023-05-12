
N = [1,2,3,4]
M = 2

# 순열
from itertools import permutations

lst1 = list(permutations(N, M))

#print(lst1)
for l in lst1 :
    print(l)

print('--------------------')
# 조합
from itertools import combinations

lst2 = list(combinations(N, M))

for l in lst2 :
    print(l)

print('--------------------')

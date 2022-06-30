from itertools import combinations, permutations

nums = [1,2,3,4]

# 2개를 뽑는다고 가정
perm = list(permutations(nums, 2))
print(perm)

combi = list(combinations(nums, 2))
print(combi)


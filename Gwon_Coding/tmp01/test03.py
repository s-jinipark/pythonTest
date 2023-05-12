from itertools import combinations
from itertools import permutations


a, b = map(int, input().split())

num = []
for i in range(1,a+1):
    num.append(i)

lst =  permutations(num, b)
print(list(lst))
#lst = list(lst)
lst2 = list(permutations(num, b))
for i in lst2 :
    for j in range(b):
        print( i[j], end=' ')
    print()

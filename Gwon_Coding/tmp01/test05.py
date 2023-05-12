from itertools import combinations

# N, M = map(int, input().split())

N = 4
M = 2
lst = []
test1 = []

for i in range(1, N+1) :
    lst.append(i)

test1 = list(combinations(lst, M))

#print(test1)
for t in test1:
    for j in range(M) :
        print(t[j], end= ' ')
    print()
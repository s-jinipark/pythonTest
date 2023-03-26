

N, K = 5, 2
inp = '4 1 2 3 5'

A = list(map(int, inp.split()))
#print(A)

# 생각나는 대로
# my ->
A.sort()
print(A, A[K-1])

# <= my

# 퀵 정렬로
print('--------------------')




N = 5
A = [5,2,3,4,1]

# 버블
print('--------------------')
print(A)

for i in range(N):
    for j in range(N-1-i):  # ***
        print(i, '-', A)
        if A[j] > A[j+1] :
            tmp = A[j]
            A[j] = A[j + 1]
            A[j + 1] = tmp
print(A)

# 선택
print('--------------------')
''''
구현 복잡하고, 시간 복잡도도 효율적이지 않아
코딩 테스트에서는 많이 사용하지 않음
'''
print(A)
for i in range(len(A)) :
    Max = i
    print(i, '-', A)
    for j in range(i+1, len(A)) :
        if A[Max] < A[j] :
            Max = j
    if A[i] < A[Max]:  # 여기서 실제... [위에서 한번에 해도 될 듯...]
        tmp = A[i]
        A[i] = A[Max]
        A[Max] = tmp
print(A)



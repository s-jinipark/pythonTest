

N = 10  # 수의 개수
'''
주어진 N 개의 수에서 다른 두 수의 합으로 표현되는 수 -> '좋은 수'

[?]
결국 하나씩 훑으면서 두 수의 합과 비교
=> 합 구하기랑 유사함
'''

inp = '1 2 3 4 5 6 7 8 9 10'

A = list(map(int, inp.split()))
print(A)

A.sort()

result = 0

for k in range(N) :
    find = A[k]
    i = 0
    j = N-1
    while i < j :  # 투 포인터 알고리즘
        if A[i] + A[j] == find :  # [이 아래 왜케 복잡함?]
            if i != k and j != k :
                result += 1
                print(find, '>', A[i], A[j])
                break
            elif i == k :
                i += 1
            elif j == k :
                j -= 1
        elif A[i] + A[j] < find :
            i += 1
        else :
            j -= 1
print(result)

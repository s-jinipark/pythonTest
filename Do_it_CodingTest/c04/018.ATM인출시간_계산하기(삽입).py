
N = 5  # 데이터의 개수
inp = '3 1 4 3 2'
A = list(map(int, inp.split()))

print(A)

'''
삽입 정렬
이미 정렬된 데이터 범위에 정렬되지 않은 데이터를 적절한 위치에 삽입시켜 정렬하는 방식
시간복잡도는 느린 편이지만 구현하기 쉬움

(핵심)
선택 데이터를 현재 정렬된 데이터 범위 내에서 적절한 위치에 삽입하는 것이 삽입 정렬의 핵심

[my]
바깥쪽 루프에서  하나씩 가고 
안쪽 루프에서는 앞에 있는 거 값 확인

'''
for i in range(1, N):  # 삽입 정렬
    insert_point = i
    insert_value = A[i]
    for j in range(i-1, -1, -1) :
        #print(i, ' - ', j)
        if A[i] > A[j]:
            insert_point = j+1
            break
        if j == 0 :
            insert_point = 0

    for j in range(i, insert_point, -1):
        A[j] = A[j-1]
    A[insert_point] = insert_value
    print(i, ' > ' , A)
print(A)

# 합 배열 만들기
S = [0]*N
print(S)
S[0] = A[0]  # 따로 넣어 줌

for i in range(1, N):
    S[i] = S[i-1] + A[i]
print(S)

sum = 0
for i in range(N):
    sum += S[i]
print(sum)

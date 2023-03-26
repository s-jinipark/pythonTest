

N = 5
inp = '3 1 4 3 2'

A = list(map(int, inp.split()))
#print(A)

# 생각나는 대로
# my ->
A.sort()
print(A)

B = []
sum = 0
for i in range(N):
    if i == 0 : # 0 일땐 예외
        B.append(A[i])
        sum += A[i]
    else :
        B.append(B[i-1]  + A[i])
        sum +=  (B[i - 1] + A[i])
print(B)
print(sum)
# <= my

# 삽입 정렬로
print('--------------------')
for i in range(1, N) : # 삽입 정렬 1 부터
    ins_point = i
    ins_value = A[i]
    #print('>')
    # j 는 0 , 1 0 , 2 1 0, 3 2 1 0 순서로 ...
    for j in range(i-1, -1, -1): # 뒤에서 부터 올 필요가 있는지 ??  for j in range(i) 하면 안됨?
    #for j in range(i):  # 이거 안 됨
        #print(j)
        if A[j] < A[i]:
            ins_point = j+1
            break
        if j == 0 :
            ins_point = 0

    for j in range(i , ins_point, -1):
        A[j] = A[j-1]  # 데이터를 한 칸씩 뒤로 밀기
    A[ins_point] = ins_value  # 삽입 위치에 데이터 저장

print(A)


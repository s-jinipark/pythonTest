
print("1. 별찍기")
for i in range(1, 6) :
    print('*' * i)

# 책에는 ?? [이어 나오는 다른 별찍기에 활용할려구 2중으로 쓴 듯]
n = 5
for i in range(n):
    for j in range(i+1):
        print('*', end='')  # 출력위치를 다음 줄로 넘기는 것을 방지
    print()


print("--------------------")
print("2. 별찍기 - 오른쪽 정렬")

for i in range(n):
    for j in range(n-i-1):   # 처음에 여기를 (n-i) 로 해서 한 칸 띄어 짐
        print(' ', end='')
    for k in range(i+1):
        print('*', end='')
    print()


print("--------------------")
print("3. 별찍기 - 첫번째 별1, 둘째 별3, N번째 별 2*N-1 ")
# 처음에는 위의 1, 2 를 짬뽕 (붙일 생각)

for i in range(n):
    for j in range(n-i-1):
        print(' ', end='')
    for k in range(i+1):
        print('*', end='')
    for l in range(i):
        print('*', end='')
    print()
#=> 되기는 됨

for i in range(n):
    for j in range(n-i-1):
        print(' ', end="")
    for j in range(2*i +1):
        print('*', end="")
    print()

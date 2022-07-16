
print("1. 별찍기")
for i in range(1, 6) :
    print('*' * i)

# 책에는 ?? [다음 별찍기에 활용할려구 2중으로 쓴 듯]
n = 5
for i in range(n):
    for j in range(i+1):
        print('*', end="")
    print()

print("--------------------")
print("2. 별찍기 - 오른쪽 정렬")
for i in range(n):
    for j in range(n-i):
        print(' ', end="")
    for j in range(i+1):
        print('*', end="")
    print()

# 책에는 ?? 공백을 나는 n-i 로 해서
# 책 n-i-1 와 다름 .. 내가 공백이 하나 더 있음.. ㅠ..
for i in range(n):
    for j in range(n-i-1):
        print(' ', end="")
    for j in range(i+1):
        print('*', end="")
    print()


print("--------------------")
print("3. 별찍기 - 첫번째 별1, 둘째 별3, N번째 별 2*N-1 ")

for i in range(n):
    for j in range(n-i-1):
        print(' ', end="")
    for j in range(2*i +1):
        print('*', end="")
    print()


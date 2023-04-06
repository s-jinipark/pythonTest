
def facto(v):
    if v == 1:
        return 1
    else :
        return v * facto(v-1)

res = facto(6)
print(res)

'''
4 -> 24
5 -> 120
6 -> 720
7 -> 5040
'''

print('--------------------')

'''
[이거 가지고...]
1. n개의 원반을 A에서 C로 옮기기 위해, n-1개의 원반을 A에서 B로 옮깁니다.
2. 가장 큰 원반을 A에서 C로 옮깁니다.
3. B에 있는 n-1개의 원반을 C로 옮깁니다.

'''

def hanoi(num, start, to, end):
    if num == 1 :
        print(start, end)
    else:
        hanoi(num-1, start, end, to)
        print(start, end)
        hanoi(num-1, to, start, end)

num = 2
hanoi(num, 1, 2, 3)

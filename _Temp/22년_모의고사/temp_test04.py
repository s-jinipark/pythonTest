
# 바이너리 서치


a = [3, 15, 5, 3, 6, 2, 35, 77, 23, 125]

def bs(s, e, target) :
    while s <= e :   # 엇갈리지 않을 때까지
        mid = (s + e) // 2
        if a[mid] == target : return mid
        if a[mid] < target : s = mid +1
        else : e = mid -1
    return -1

target = 35
a.sort()
print(a)

print(bs(0, 9, 35))
print('==============================')

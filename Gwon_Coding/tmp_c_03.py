
# 블래잭이니까 3장 고르기

n, m = map(int, input().split())
#lst = list( map(int, input().split()) )
lst = [93, 181, 245, 214, 315, 36, 185, 138, 216, 295]
max = 0

# for i in range(len(lst) - 2 ):
#     for j in range(i+1, len(lst) - 1):
#         for k in range(i+2, len(lst) ):
for i in range(0, len(lst)-2):
    for j in range(i+1 ,  len(lst)-1 ):
        for k in range(j+1 , len(lst)):
            #print( i, j , k, '>', lst[i], lst[j], lst[k], '=', lst[i] + lst[j] + lst[k])
            #print(lst[i] + lst[j] + lst[k])
            tmp = lst[i] + lst[j] + lst[k]
            if tmp <= m and tmp > max :
                max = tmp
                print(i, j, k, '>', lst[i], lst[j], lst[k], '=', lst[i] + lst[j] + lst[k])
print(max)
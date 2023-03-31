

inp = '2143'
lst = []

for i in inp :
    lst.append(int(i))

print(lst)

'''
이건 앞에서 부터 채워나감
겉의 i 가 증가하면서 하나씩
 안의 j 에서 max 찾아서 i 와 교체
'''
for i in range(len(lst)) :
    Max = i
    for j in range(i+1, len(lst)) :
        if lst[j] > lst[Max] :
            Max = j
    if lst[i] < lst[Max] :
        tmp = lst[i]
        lst[i] = lst[Max]
        lst[Max] = tmp

print(lst)
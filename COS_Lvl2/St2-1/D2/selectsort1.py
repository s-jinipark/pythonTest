# 선택 정렬  인덱스 0부터 정렬

def swap(data, a, b):
    global cnt
    tmp = data[a]
    data[a] = data[b]
    data[b] = tmp


def selectsort(tmplist):
    for i in range(len(tmplist)):
        minidx = i

        for j in range(i+1, len(tmplist)):
            if tmplist[j] < tmplist[minidx]:
                minidx = j
        if minidx != i:
            swap(tmplist, minidx, i)


tmplist = [10, 2, 6, 4, 3, 7, 5 ]
selectsort(tmplist)
print(tmplist)




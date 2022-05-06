# 선택 정렬  인덱스 0부터 정렬

def swap(data, a, b):
    global cnt
    cnt +=1
    tmp = data[a]
    data[a] = data[b]
    data[b] = tmp


def selectsort(tmplist):
    for i in range(len(tmplist)-1, -1, -1):
        maxidx = i

        for j in range(i-1, -1, -1):
            if tmplist[j] < tmplist[maxidx]:
                maxidx = j
        if maxidx != i:
            swap(tmplist, maxidx, i)
        print(tmplist)


tmplist = [10, 2, 6, 4, 3, 7, 5 ]
cnt = 0
selectsort(tmplist)
print(tmplist)
print(cnt)



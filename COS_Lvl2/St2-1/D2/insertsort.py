# 삽입 정렬
tmplist = [10, 2, 6, 4, 3, 7, 5 ]
print(tmplist)

for i in range(1, len(tmplist)):
    standard = tmplist[i]
    idx = i - 1  # 1

    while idx >= 0 and standard < tmplist[idx]:
        tmplist[idx+1] = tmplist[idx]
        idx -= 1

    tmplist[idx + 1] = standard
    print(tmplist)


















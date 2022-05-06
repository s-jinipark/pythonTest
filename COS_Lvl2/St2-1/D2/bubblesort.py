# 버블 정렬
tmplist = [10, 2, 6, 4, 3, 7, 5 ]
# 2 10 7 4 3 7 D5
# 2 7 4 3 7 D5 10

for i in range(len(tmplist)):
    for j in range(len(tmplist)-1):
        if tmplist[j] > tmplist[j+1]:
            tmp = tmplist[j]
            tmplist[j] = tmplist[j+1]
            tmplist[j+1] = tmp
    print(tmplist)


















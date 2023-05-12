
import sys
input = sys.stdin.readline


#cnt = int(input())
cnt = 5

# lst=[list([map(int, input().split())]) for _ in range(cnt)]
# => [[<map object at 0x000001CCD51DB1F0>], [<map object at 0x000001CCD51DBA30>]]
#lst=[list(map(int, input().split())) for _ in range(cnt)]

lst = [[5, 50, 50, 70, 80, 100], [7, 100, 95, 90, 80, 70, 60, 50],
        [3, 70, 90, 80], [3, 70, 90, 81], [9, 100, 99, 98, 97, 96, 95, 94, 93, 91]
       ]
print(lst)

for l in lst :
    tmp_sum = 0
    for i in range(1, l[0]+1):
        print(l[i])
        tmp_sum += l[i]
    print(tmp_sum/l[0])
    avg = tmp_sum/l[0]
    avg_cnt = 0
    for j in range(1, l[0]+1):
        if l[j] > avg :
            avg_cnt += 1
    print('>', round(avg_cnt/l[0] *100, 3) )
    tmp_f = "{:.3f}%".format(avg_cnt/l[0] *100)
    print(tmp_f)

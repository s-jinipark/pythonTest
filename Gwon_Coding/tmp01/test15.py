
import sys
input = sys.stdin.readline


#cnt = int(input())
cnt = 3
#in_list = list(map(int, input().split()))
in_list = [10, 20, 30]
result = [0] * cnt
#print(cnt, in_list)

M = max(in_list)
#print(M)
new_sum = 0
for i in in_list :
    #result[i] = in_list[i]/M *100
    #tmp = in_list[i]/M *100
    tmp = i/M * 100
    print(tmp)
    new_sum += tmp
print(new_sum/cnt)
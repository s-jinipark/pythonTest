
import sys
input = sys.stdin.readline


M = 10
in_list = []


# for _ in range(M):
#     a = int(input())
#     in_list.append(a)

in_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#in_list = [42, 84, 252, 420, 840, 126, 42, 84, 420, 126]
result = [0] * M
print(in_list)
#print(result)

dic = {}
# 나머지 구하기
for i in in_list :
    tmp = i%42
    print(tmp)
    if tmp not in dic:
        dic[tmp] = 1
    else :
        dic[tmp] += 1
print(len(dic))

import sys

sys.stdin = open("input10-4.txt", "rt")
case = int(input())
#print(case)
for i in range(case) :
    n = int(input())
    dic = {}
    ans = 1
    for j in range(n):
        #nm, ct = map(str, input().split())
        nm, ct = input().split()   # 그냥
        print(nm, ct)
        if ct in dic :
            dic[ct] += 1
        else:
            dic[ct] = 1

    print(dic)
    print('--------------------')
    for k in dic.keys() :
        print(k)
        ans = ans * (dic[k]+1)
    ans -= 1
    print('---------------', ans)
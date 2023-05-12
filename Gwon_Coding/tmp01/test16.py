
import sys
input = sys.stdin.readline


#cnt = int(input())
cnt = 5

# in_list = []
# for _ in range(cnt):
#      a = input()
#      in_list.append(a)
#
# print(cnt, in_list)

# strip() 은 '\n' 제거 위해서
# str=[input().strip() for _ in range(cnt)]
# print(str)

str = ['OOXXOXXOOO', 'OOXXOOXXOO', 'OXOXOXOXOXOXOX', 'OOOOOOOOOO', 'OOOOXOOOOXOOOOX']
print(str)

for s in str :
    #print(s)
    tmp_sum = 0
    result = [0] * len(s)
    for i in range(len(s)):
        print(s[i] , end= ' ')
        if s[i]  == 'O' :
            result[i] =1
            if i > 0 and result[i-1] >0 :
                result[i] += result[i-1]
    print(sum(result))



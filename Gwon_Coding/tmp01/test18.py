
# import sys
# input = sys.stdin.readline


# n = int(input())
# str = input()
#
# #print(n, str)
#
# tmp_sum = 0
# for i in range(n):
#     tmp_sum += int(str[i])
# print(tmp_sum)


#str = input()
# str = 'baekjoon'
#
# result = [-1]* 26
#
# for i in range(len(str)) :
#     # 결국 a = 0 , z = 25 로 계산
#     print( ord(str[i] ) - 97 )
#     tmp = ord(str[i] ) - 97
#     if result[tmp] == -1 :
#         result[tmp] = i
# print(result)
#
# for j in result :
#     print(j, end=' ')


#n = int(input())
n = 2

#lst = [input().split() for _ in range(n)]
# for _ in range(n):
#     a, b = input().split()
# print(a, b)
# lst = [['3', 'ABC'], ['5', '/HTP']]
#
# print(lst)
#
# for l in lst:
#     tmp = ''
#     for j in range(len(l[1])) :
#         print(l[1][j])
#         tmp += l[1][j] * int(l[0])
#     print(tmp)

# for i in range(n):
#     a, b = input().split()
#     for j in range(len(b)):
#         print(b[j] * int(a), end='')
#     print()


# str = input()
#
# str = str.upper()
# print(str)
#
# dic = {}
# for s in str:
#     if s not in dic :
#         dic[s] = 1
#     else :
#         dic[s] += 1
# print( max(dic))
# prt = max(dic)
# max_cnt = dic[prt]
# print(max_cnt)
# #print(dic.keys())
# print(dic.values())
# lst = list(dic.values())
# lst.sort(reverse=True)
# print(lst)
# print(lst[0], lst[1])
# if lst[0] != list[1] :
#     print('?')
# else :
#     print(prt)
#
# # 맥스 값을 알아내고 그걸 카운트
# print(lst.count(max_cnt))

##### 정리해서 다시 해보면
# (통과 안됨)

# import sys
# input = sys.stdin.readline
#
# #str = input()
# #str = 'Mississipi'
# str = 'k'
#
# str = str.upper()
# print(str)
#
# dic = {}
# for s in str:
#     if s in dic :
#         dic[s] += 1
#     else :
#         dic[s] = 1  # 신규
#
# print(dic)
# max_s = max(dic)
# print(max_s)
# print(dic[max_s])
# max_n = dic[max_s]
# print(list(dic.values()).count(max_n))
# dup_chk = list(dic.values()).count(max_n)
# if dup_chk > 1 :
#     print('?')
# else :
#     print(max_s)


#str = input()
#str = 'Mississipi'
# str = 'k'
#
# str = str.upper()
# print(str)
#
# lst = list(str)
# lst2 = list(set(lst))
# print(lst2)
#
# dic = {}
# lst3 = []
# for i in lst2:
#     #print(lst.count(i))
#     print(str.count(i))  # 오! 이것도 됨
#     dic[i] = str.count(i)
#
# print(dic)
# print(dic[max(dic)] )
# print(list(dic.values()).count(  dic[max(dic)] ))
#
# chk = list(dic.values()).count(  dic[max(dic)] )
# if chk >1 :
#     print('?')
# else :
#     print(max(dic))


# 딕셔너리에 넣지 않으면 될 것 같다는 ...
# 복습 필요

#str = input()
#str = 'Mississipi'
str = 'k'

str = str.upper()
print(str)

uniq_w = list(set(str))
print(uniq_w)

cnt_lst = []
for u in uniq_w :
    cnt_lst.append(str.count(u))

print(cnt_lst)

if cnt_lst.count(max(cnt_lst)) > 1:
    print('?')
else :
    max_idx = cnt_lst.index(max(cnt_lst))
    #print(max_idx)
    print(uniq_w[max_idx])


# 또한 문자열은 공백으로 시작하거나 끝날 수 있다.
#inp = ' The Curious Case of Benjamin Button'
inp = ' '
inp = inp.strip()

lst = inp.split(' ')
print(lst)
if len(lst) == 1 and lst[0] == '' :
    print(0)
else :
    print(len(lst))

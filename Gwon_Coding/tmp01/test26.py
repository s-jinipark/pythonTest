

#A, B = map(int, input().split())

# A, B = 1, 2
# print(A, B)
#
# if A > B :
#     print('>')
# elif A < B :
#     print('<')
# elif A == B :
#     print('==')

#i = int(input())
# i = 100
#
# if i >= 90 :
#     print('A')
# elif 90 > i >= 80 :
#     print('B')
# elif 80 > i >= 70 :
#     print('C')
# elif 70 > i >= 60 :
#     print('D')
# else :
#     print('F')


#y = int(input())
# y = 1999 #2000
#
# if y%4 ==0 and (y%100 != 0 or y%400 == 0) :
#     print(1)
# else :
#     print(0)
#

#x = int(input())
#y = int(input())
# x = 12
# y = 5
#
# if x >= 0 and y >= 0 :
#     print(1)
# elif x < 0 and y >= 0 :
#     print(2)
# elif x < 0 and y < 0 :
#     print(3)
# elif x >= 0 and y < 0 :
#     print(4)

#A, B = map(int, input().split())
#A, B = 10, 10
#A, B = 0, 30
# A, B = 23, 40
# print(A, B)
# #print(B-45+60)
# # 일단 45 빼
# B -= 45
# if B <0 :
#     B += 60
#     A -= 1
#     if A < 0 :
#         A += 24
# print(A, B)

# #S, M = map(int, input().split())
# #T =  int(input())
# # S, M = 17, 40
# # T =  80
# S, M = 23, 48
# T =  25
#
# print ((M+T)//60)
#
# # 일단 더해서 60 이 넘는지 본다
# M = M+T
# if M >= 60 :
#     S += M//60   # 몫
#     M = M%60    # 나머지
#     if S >=24 :
#         S -= 24
# print(S, M)
#




# 리스트에 넣고 set 변환 하면 될 듯

#num = list(map(int, input().split()))
# num = [3,3,6]
#
# st = set(num)
# print(st)
# num2 = list(st)
#
# if len(st) == 1 :
#     print(10000 + num2[0] * 1000)
# elif len(st) == 2 :
#     print(1000 + num2[-1] * 100)

#--> 이건 못 품


##### ##### ##### ##### ##### #####

#n = int(input())
n = 5
lst = [5,2,3,4,1]
for i in range(5):
    lst.append(int(input()))

lst.sort()
print(lst)
for l in lst:
    print(l)
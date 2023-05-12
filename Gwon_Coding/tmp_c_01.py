

#a, b = map(int, input().split())
# a, b = 7,3
# print(a+b)
# print(a-b)
# print(a*b)
# print(int(a/b))
# print(a%b)


# a = int(input())
# print(a-543 )


# # 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개
# org = [1,1,2,2,2,8]
# lst = list(map(int, input().split()))
#
# #print(lst)
# for i in range(len(org)):
#     lst[i] = org[i] - lst[i]
#     print(lst[i], end=' ')


# A, B, C = map(int, input().split())
#
# print( (A+B)%C )
# print( ((A%C) + (B%C))%C )
# print( (A*B)%C )
# print( ((A%C) * (B%C))%C )


# a = input()
# b = input()
#
# n1 = int(a)
# n3 = n1 * int(b[2])
# n4 = n1 * int(b[1])
# n5 = n1 * int(b[0])
# print(n3)
# print(n4)
# print(n5)
# print(n3+n4*10+n5*100)


# print("\    /\\")
# print(" )  ( ')")
# print("(  /  )")
# print(" \(__)|")
#
# print()
#
# print("|\_/|")
# print("|q p|   /}")
# print("( 0 )\"\"\"\\")
# print("|\"^\"`    |")
# print("||_/=\\\\__|")
#
# print()
#
# print("         ,r'\"7")
# print("r`-_   ,'  ,/")
# print(" \. \". L_r'")
# print("   `~\/")
# print("      |")
# print("      |")


A = int(input())
B = int(input())
C = int(input())

multi = A*B*C

cnt = [0] *10
# 3 자리 라는 전제

tmp = str(multi)

for i in range(len(tmp)):
    cnt[int(tmp[i])] += 1

#print(cnt)
for c in cnt:
    print(c)


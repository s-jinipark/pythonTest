
# 문자열로 입력
# a, b = input().split()
# print(a, b)
#
# rev_a = a[::-1]
# rev_b = b[::-1]
# print(rev_a, rev_b)
#
# print(max(int(rev_a), int(rev_b) ))


# #str = input()
# #str = 'WA'
# str = 'UNUCIC'
# # 알파벳에 맞게 아스키 활용 A 는 0 번째, B는 1번째
# # 시간을 넣어놓는다 (숫자 2에 ABC 가 있고 1이 2초 걸리고 숫자가 커지면 +1 이므로
# a_time = [3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,8,9,9,9,10,10,10,10]
#          #A B C D E F G H I J K L M N O P Q R S T U V  W  X  Y  Z
# # 뒤에 두 자리는 4개씩
#
# tot = 0
# for s in str:
#     tot += a_time[ord(s)-65]
#     #print(ord(s)-65)
#
# print(tot)


#str = input()
# str = 'ljes=njak'
# cro_words = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
#
# tmp_idx = 0
# tmp_cnt = 0
#
# for c in cro_words :
#     while tmp_idx > -1 :
#         tmp_idx = str.find(c, tmp_idx)
#         print(tmp_idx)
#         if tmp_idx != -1:
#             tmp_idx += len(c)
#         else :
#             tmp_cnt += 1
#
# print(tmp_cnt)
# #print( str.find('lji') )


# 크로아티아
#str = input()
str = 'ljes=njak'
cro_words = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

tmp_idx = 0
tot = 0
while tmp_idx < len(str):
    # 크로아티아 알파벳 찾기
    for c in cro_words :
        f_idx = str.find(c, tmp_idx)
        #print(c, '>', f_idx, tmp_idx)
        if f_idx == tmp_idx :
            print('>>' , c)
            tmp_idx += len(c)
            tot += 1
            break
    else:
        print(str[tmp_idx])
        tmp_idx += 1
        tot += 1

print(tot)

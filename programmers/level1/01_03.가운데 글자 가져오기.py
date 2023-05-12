def solution(s):
    answer = ''
    len_s = len(s)
    mid = int(len_s/ 2)
    even = True
    if len_s % 2 != 0 :
        even = False

    if even :
        print(s[mid-1:mid+1])
    else :
        print(s[mid])
    return answer

#s = 'abcde'
s = 'qwer'

re = solution(s)
print(re)

print("====================")

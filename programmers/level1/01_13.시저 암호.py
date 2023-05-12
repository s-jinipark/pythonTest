def solution(s, n):
    answer = ''

    for i in s :
        #print(ord(i))
        if i == ' ':
            answer += ' '
            continue

        ord_num = ord(i)
        ord_num2 = ord_num +n
        #print(ord_num)

        # if (97 <= ord_num <= 122) and ord_num2 > 122 :
        #     print('-> ', ord_num2 - 26)
        #     print(chr(ord_num2 - 26))
        #     answer += chr(ord_num2 - 26)
        # elif (65 <= ord_num <= 90) and ord_num2 > 90:
        #     print('=> ', ord_num2 - 26)
        #     print(chr(ord_num2 - 26))
        #     answer += chr(ord_num2 - 26)
        # else:
        #     answer += chr(ord_num2)

        if ( ((97 <= ord_num <= 122) and ord_num2 > 122 )  or
            ( (65 <= ord_num <= 90) and ord_num2 > 90 )  ):
            print('-> ', ord_num2 - 26)
            print(chr(ord_num2 - 26))
            answer += chr(ord_num2 - 26)
        else:
            answer += chr(ord_num2)

    return answer


#s = "azAZ"
'''
97
122
65
90
'''
#s = "AB"
#s = 'z'
s = "a B z"
n = 4

re = solution(s, n)
print(re)

print("====================")


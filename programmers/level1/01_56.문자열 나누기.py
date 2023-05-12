def solution(s):
    answer = 0
    idx = 0
    first_ch = ""
    first_cnt = 0
    other_cnt = 0
    test = ''

    for i in range(len(s)):
        if first_ch == "" :
            first_ch = s[i]
            first_cnt = 1
            test += s[i]
        else :  # 값이 있다는 ...
            if first_ch == s[i] :
                first_cnt += 1
                test += s[i]
            else :
                other_cnt += 1
                test += s[i]
        print(test)
        # 여기서 자름
        if first_cnt == other_cnt :
            first_ch = ""
            answer += 1
            first_cnt = 0
            other_cnt = 0
            print('>', test)
            test = ""
        else : # 여기는 나머지
            if i == len(s)-1:  # 마지막 까지 왔다면
                #first_ch = ""
                answer += 1
                print('=>>', test)

    # 첫 시도 2개로 잘림
    # if 문을 2단계로 나눠야 함
    # for i in range(len(s)):
    #     if first_ch == "" :
    #         first_ch = s[i]
    #         first_cnt = 1
    #         test += s[i]
    #     else :  # 값이 있다는 ...
    #         if first_cnt == other_cnt :
    #             first_ch = ""
    #             answer += 1
    #             first_cnt = 0
    #             other_cnt = 0
    #             test += s[i]
    #             print(test)
    #             test = ""
    #         else :  # cnt 가 다를 경우
    #             if first_ch == s[i] :
    #                 first_cnt += 1
    #                 test += s[i]
    #             else :
    #                 other_cnt += 1
    #                 test += s[i]

    return answer


#s = "banana"
#s = "abracadabra"
s = "aaabbaccccabba"

re = solution(s)
print(re)

print("====================")


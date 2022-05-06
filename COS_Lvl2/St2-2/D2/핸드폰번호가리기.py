def solution(phone_number):
    #answer = 0
    answer = ''

    len_p = len(phone_number) -4

    for i in range(len(phone_number)):
        if i < len_p :
            answer += '*'
        else :
            answer += phone_number[i]

    return answer




#sample 1
phone_number = "01033334444"
res = solution(phone_number)
print(res)

#sample 1
phone_number = "027778888"
res = solution(phone_number)
print(res)

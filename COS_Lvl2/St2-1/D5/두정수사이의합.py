def solution(a, b):
    answer = 0
    if a > b :
        st_n = b
        ed_n = a
    else :
        st_n = a
        ed_n = b

    for i in range(st_n, ed_n+1):
        answer += i
    print(answer)
    return answer




#sample 1
a = 3
b = 5
res = solution(a, b)

#sample 1
a = 3
b = 3
res = solution(a, b)


#sample 1
a = 5
b = 3
res = solution(a, b)

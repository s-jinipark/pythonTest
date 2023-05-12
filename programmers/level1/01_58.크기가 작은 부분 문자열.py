def solution(t, p):
    answer = 0
    p_len = len(p)

    for i in range(0, len(t)-p_len+1):
        tmp = t[i:i+p_len]
        print(tmp)
        if int(tmp) <= int (p):
            answer += 1

    return answer


#t = "3141592"
#p = "271"

t = "500220839878"
p = "7"

re = solution(t, p)
print(re)

print("====================")



def solution(num, k):
    answer = 0
    tmp = 0
    while tmp < num :
        tmp += k
        if tmp >= num :
            break
        answer += tmp
        print(tmp)

    return answer


num = 20
k = 5

an = solution(num, k)

print(an)